from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=50)
    password = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
