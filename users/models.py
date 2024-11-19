from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import NULLABLE


class UserRoles(models.TextChoices):
    """класс для ролей"""
    MEMBER = 'member', _('member')
    MODER = 'moder', _('moder')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=25, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=6, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
