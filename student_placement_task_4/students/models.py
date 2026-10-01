from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class Student(models.Model):
    """Table drawn on the whiteboard: id | s_name | s_pass | s_email"""
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100, unique=True)
    s_pass = models.CharField(max_length=128)  # stored hashed
    s_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw):
        self.s_pass = make_password(raw)

    def check_password(self, raw):
        return check_password(raw, self.s_pass)

    def __str__(self):
        return self.s_name


class PredictionRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="predictions")
    cgpa = models.FloatField()
    iq = models.FloatField()
    profile_score = models.FloatField()
    placed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
