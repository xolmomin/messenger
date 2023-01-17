from django.db import models
from django.db.models import ManyToManyField

from shared.models.base import BaseModel


class Group(BaseModel):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to='groups/', default='groups/default.jpg')
    bio = models.CharField(max_length=255)
    username = models.CharField(max_length=32, unique=True, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    owner = models.ForeignKey('users.User', models.SET_NULL, null=True, blank=True)
    user = ManyToManyField('users.User')
