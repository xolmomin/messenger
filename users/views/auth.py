from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.forms import SignUpForm
from users.models import User


#  TODO: Editing later / because i can't add ""Device model"" / users add manually
class UserSignUpView(CreateView):
    template_name = 'users/auth/signup.html'
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('auth_signin')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserSignInView(TemplateView):
    template_name = 'users/auth/signin.html'


class UserResetPasswordView(TemplateView):
    template_name = 'users/auth/reset-password.html'


class UserLockScreenView(TemplateView):
    template_name = 'users/auth/lockscreen.html'
