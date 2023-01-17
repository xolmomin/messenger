from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from shared.utils.validators import phone_regex


class User(AbstractUser):
    class Theme(TextChoices):
        WHITE = 'white', 'Oq'
        BLACK = 'black', 'Qora'

    email = models.EmailField(_("email address"), unique=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=150, unique=True, null=True, validators=[username_validator])
    image = models.ImageField(upload_to='users/', default='users/default.jpg')
    bio = models.CharField(max_length=355, null=True, blank=True)
    phone = models.CharField(max_length=9, validators=[phone_regex])
    theme = models.CharField(max_length=25, choices=Theme.choices, default=Theme.WHITE)
    is_online = models.BooleanField(default=False)
    social = models.JSONField(default=dict)
