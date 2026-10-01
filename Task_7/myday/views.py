from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Question, TestResult


# =========================
# HOME
# =========================

def home(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('myday:home')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(request, 'home.html')


# =========================
# SIGNUP
# =========================

def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect('myday:signup')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=name
        )

        login(request, user)

        return redirect('myday:home')

    return render(request, 'signup.html')


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('myday:home')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(request, 'login.html')


# =========================
# LOGOUT
# =========================

def logout_view(request):

    logout(request)

    return redirect('myday:home')


# =========================
# TEST FUNCTION
# =========================

@login_required(login_url='myday:login')
def test_page(request, test_number):

    questions = Question.objects.filter(
        test_number=test_number
    )

    if request.method == 'POST':

        right = 0
        wrong = 0

        for question in questions:

            answer = request.POST.get(
                f'question_{question.id}'
            )

            if answer:

                if answer == question.correct_option:

                    right += 1

                else:

                    wrong += 1

        total = questions.count()

        points = 0

        if total > 0:
            points = (right / total) * 10

        TestResult.objects.create(

            user=request.user,

            test_number=test_number,

            total_questions=total,

            right_answers=right,

            wrong_answers=wrong,

            points=round(points, 2)
        )

        return render(
            request,
            'result.html',
            {
                'test_number': test_number,
                'total': total,
                'right': right,
                'wrong': wrong,
                'points': round(points, 2),
            }
        )

    return render(
        request,
        'test.html',
        {
            'questions': questions,
            'test_number': test_number
        }
    )


# =========================
# TEST HISTORY
# =========================

@login_required(login_url='myday:login')
def test_history(request):

    results = TestResult.objects.filter(
        user=request.user
    ).order_by('-attempted_at')

    total_tests = results.count()

    if total_tests > 0:

        total_points = sum(
            result.points
            for result in results
        )

        average_score = round(
            total_points / total_tests,
            2
        )

    else:

        average_score = 0

    return render(
        request,
        'test_history.html',
        {
            'results': results,
            'total_tests': total_tests,
            'average_score': average_score,
        }
    )