from django import forms

from .models import Student


class RegisterForm(forms.Form):
    s_name = forms.CharField(label="Name", max_length=100)
    s_email = forms.EmailField(label="Email")
    s_pass = forms.CharField(label="Password", min_length=6, widget=forms.PasswordInput)

    def clean_s_name(self):
        name = self.cleaned_data["s_name"].strip()
        if Student.objects.filter(s_name__iexact=name).exists():
            raise forms.ValidationError("This name is already registered.")
        return name

    def clean_s_email(self):
        email = self.cleaned_data["s_email"].lower()
        if Student.objects.filter(s_email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class LoginForm(forms.Form):
    s_name = forms.CharField(label="Name", max_length=100)
    s_pass = forms.CharField(label="Password", widget=forms.PasswordInput)


class PredictionForm(forms.Form):
    cgpa = forms.FloatField(label="CGPA", min_value=0, max_value=10,
                            widget=forms.NumberInput(attrs={"step": "0.01"}))
    iq = forms.FloatField(label="IQ", min_value=50, max_value=200,
                          widget=forms.NumberInput(attrs={"step": "1"}))
    profile_score = forms.FloatField(label="Profile Score", min_value=0, max_value=100,
                                     widget=forms.NumberInput(attrs={"step": "1"}))
