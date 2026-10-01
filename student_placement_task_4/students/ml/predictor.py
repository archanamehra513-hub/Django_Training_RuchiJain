"""Loads the scaler + SVC once and exposes predict()."""
from functools import lru_cache

import joblib
import pandas as pd
from django.conf import settings

FEATURES = ["cgpa", "iq", "profile_score"]


@lru_cache(maxsize=1)
def _load():
    scaler = joblib.load(settings.ML_SCALER_PATH)
    model = joblib.load(settings.ML_MODEL_PATH)
    return scaler, model


def predict(cgpa, iq, profile_score):
    scaler, model = _load()
    X = pd.DataFrame([[cgpa, iq, profile_score]], columns=FEATURES)
    X_scaled = scaler.transform(X)
    placed = int(model.predict(X_scaled)[0])

    confidence = None
    if hasattr(model, "predict_proba"):
        try:
            confidence = float(model.predict_proba(X_scaled)[0][placed])
        except Exception:
            pass
    return {"placed": bool(placed), "confidence": confidence}
