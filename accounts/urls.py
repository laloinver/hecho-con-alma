from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrarse/', views.registrar_usuario, name='registrar_usuario'),
]
