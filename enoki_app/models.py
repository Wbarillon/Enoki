from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

from enoki_app.managers import (
    CustomUserManager
)


# Create your models here.

class CustomUser(PermissionsMixin, AbstractBaseUser):
    nickname = models.CharField(verbose_name = 'Pseudo', max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(verbose_name = 'Date de création', default = timezone.now)

    USERNAME_FIELD = 'nickname'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Utilisateur (custom)'
        verbose_name_plural = 'Utilisateurs (custom)'