# Student Placement Prediction (Django)

Flow (from the whiteboard): Home → Register / Login → Prediction form → ML model → Result page.

## Run
```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/

## Structure
- `students/models.py`   – `Student` (s_id, s_name, s_pass [hashed], s_email) and `PredictionRecord`
- `students/views.py`    – home, register, login, logout, predict (session-based auth)
- `students/ml/predictor.py` – loads `ml_models/scaler_spp.pkl` + `ml_models/mlmodel_spp.pkl` (StandardScaler + SVC)
- `templates/`           – Home, Register, Login, Prediction form, Result

Features: `cgpa`, `iq`, `profile_score` → `placed` (0/1).
The pickles were saved with scikit-learn 1.6.1, so that version is pinned in requirements.txt.
