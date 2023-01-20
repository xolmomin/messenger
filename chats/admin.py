from django.contrib import admin

# Register your models here.
from chats.models import Group, ChatMembers

admin.site.register(Group)
admin.site.register(ChatMembers)
