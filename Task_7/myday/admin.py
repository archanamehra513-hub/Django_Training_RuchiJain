from django.contrib import admin

from .models import Question, TestResult


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'test_number',
        'question',
        'correct_option'
    )

    list_filter = (
        'test_number',
    )


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'test_number',
        'total_questions',
        'right_answers',
        'wrong_answers',
        'points',
        'attempted_at'
    )

    list_filter = (
        'test_number',
        'user'
    )