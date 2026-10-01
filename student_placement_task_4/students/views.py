from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import LoginForm, PredictionForm, RegisterForm
from .ml import predictor
from .models import PredictionRecord, Student


def student_login_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.session.get("student_id"):
            messages.warning(request, "Please log in first.")
            return redirect("login")
        return view(request, *args, **kwargs)
    return wrapper


def home(request):
    return render(request, "students/home.html")


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        student = Student(s_name=form.cleaned_data["s_name"], s_email=form.cleaned_data["s_email"])
        student.set_password(form.cleaned_data["s_pass"])
        student.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")
    return render(request, "students/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        student = Student.objects.filter(s_name__iexact=form.cleaned_data["s_name"].strip()).first()
        if student and student.check_password(form.cleaned_data["s_pass"]):
            request.session["student_id"] = student.s_id
            messages.success(request, f"Welcome back, {student.s_name}!")
            return redirect("predict")
        messages.error(request, "Invalid name or password.")
    return render(request, "students/login.html", {"form": form})


def logout_view(request):
    request.session.flush()
    return redirect("home")


@student_login_required
def predict_view(request):
    form = PredictionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        result = predictor.predict(data["cgpa"], data["iq"], data["profile_score"])
        student = Student.objects.get(pk=request.session["student_id"])
        PredictionRecord.objects.create(student=student, placed=result["placed"], **data)
        return render(request, "students/result.html", {"result": result, "data": data})
    history = PredictionRecord.objects.filter(student_id=request.session["student_id"])[:5]
    return render(request, "students/predict.html", {"form": form, "history": history})
