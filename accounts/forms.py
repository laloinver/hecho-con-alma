from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class LoginForm(forms.Form):
    # username = forms.CharField(label="Usuario", max_length=50)
    # password = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.TextInput(), max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50, )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
