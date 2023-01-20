from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput, CharField
from django.http import HttpResponse

from users.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')
