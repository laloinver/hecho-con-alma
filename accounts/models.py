from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    """Extiende el Usuario de django"""
    ADMIN = 'ADMIN'
    VISITANTE = 'VISITANTE'
    SOCIO = 'SOCIO'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SOCIO, 'Socio'),
        (VISITANTE, 'Visitante'),
    )

    role = models.CharField('Role', max_length=12, choices=ROLE_CHOICES, default=VISITANTE)
    dni = models.CharField('DNI', max_length=12, null=True, blank=True)
    address = models.CharField('Domicilio', max_length=30, null=True, blank=True)
    login_number = models.IntegerField('Número de logueos', default=0, null=True, blank=True)


# class UserProfile(models.Model):
#     ADMIN = 'ADMIN'
#     VISITANTE = 'VISITIANTE'
#     SOCIO = 'SOCIO'

#     ROLE_CHOICES = (
#         (ADMIN, 'Admin'),
#         (SOCIO, 'Socio'),
#         (VISITANTE, 'Visitante'),
#     )

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

#     role = models.CharField('Role', max_length=12, choices=ROLE_CHOICES, default=VISITANTE)
#     dni = models.CharField('DNI', max_length=12, null=True, blank=True)


class Statistics(models.Model):
    login_counter = models.IntegerField(default=0, null=True, blank=True)
    number_of_visits = models.IntegerField(default=0, null=True, blank=True)
