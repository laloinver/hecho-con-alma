from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


# Create your views here.

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                user.login_number += 1
                user.save()
                return redirect('post_list')
            else:
                messages.info(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Hay errores en el formulario')
    return render(request, 'accounts/login2.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('post_list')

def registrar_usuario(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f'Usuario {new_user.username} creado!')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})
