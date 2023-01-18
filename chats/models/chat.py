from django.db import models
from shared.models.base import BaseModel


class Group(BaseModel):
    name = models.CharField(max_length=155)
    image = models.ImageField(upload_to='groups/', default='groups/default.jpg')
    bio = models.CharField(max_length=255)
    username = models.CharField(max_length=32, unique=True, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    owner = models.ForeignKey('users.User', models.SET_NULL, null=True, blank=True)
    members = models.ManyToManyField('users.User', 'members', through='chats.ChatMembers')


class ChatMembers(models.Model):
    group = models.ForeignKey('chats.Group', models.CASCADE, 'group')
    member = models.ForeignKey('users.User', models.CASCADE, 'member')
