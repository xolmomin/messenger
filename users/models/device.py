from django.db import models

from shared.models.base import BaseModel


class Device(BaseModel):
    platform = models.CharField(max_length=15)
    location = models.CharField(max_length=55)
    browser = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', models.CASCADE)
