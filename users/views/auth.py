from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from users.forms import SignUpGetVerificationForm, SignUpVerifyForm


#  TODO: Editing later / because i can't add ""Device model"" / users add manually
class SignUpGetVerificationFormView(FormView):
    template_name = 'users/auth/signup.html'
    form_class = SignUpGetVerificationForm
    success_url = reverse_lazy('auth_signup_verify')


class SignUpVerifyFormView(FormView):
    template_name = 'users/auth/signup-verify.html'
    form_class = SignUpVerifyForm

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserSignInView(TemplateView):
    template_name = 'users/auth/signin.html'


class UserResetPasswordView(TemplateView):
    template_name = 'users/auth/reset-password.html'


class UserLockScreenView(TemplateView):
    template_name = 'users/auth/lockscreen.html'
