from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    TEST_CHOICES = (
        (1, 'Test 1'),
        (2, 'Test 2'),
        (3, 'Test 3'),
    )

    test_number = models.IntegerField(
        choices=TEST_CHOICES
    )

    question = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    correct_option = models.CharField(
        max_length=1,
        choices=(
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        )
    )

    def __str__(self):
        return f"Test {self.test_number} - {self.question[:50]}"


class TestResult(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    test_number = models.IntegerField()

    total_questions = models.IntegerField()

    right_answers = models.IntegerField()

    wrong_answers = models.IntegerField()

    points = models.FloatField()

    attempted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - Test {self.test_number}"