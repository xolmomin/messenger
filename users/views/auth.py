from random import randint

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from users.forms import SignUpGetVerificationForm, SignUpForm


#  TODO: Editing later / because i can't add ""Device model"" / users add manually
class SignUpFormView(FormView):
    success_url = reverse_lazy('auth_signup')
    email = None

    def get(self, request: WSGIRequest, *args, **kwargs):
        self.email = request.COOKIES.get('email')
        super().render_to_response(super().get_context_data()).set_cookie('email_2', 'nimadur')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.email:
            data['email'] = self.email
        return data

    def get_form_class(self):
        return SignUpForm

    def get_template_names(self):
        if self.email:
            return 'users/auth/signup-verify.html'
        return 'users/auth/signup.html'

    def form_valid(self, form):
        print("Password is: ", end=' ')
        print(*(randint(0, 9) for _ in range(6)), sep='')
        return super().form_valid(form)


class UserSignInView(TemplateView):
    template_name = 'users/auth/signin.html'


class UserResetPasswordView(TemplateView):
    template_name = 'users/auth/reset-password.html'


class UserLockScreenView(TemplateView):
    template_name = 'users/auth/lockscreen.html'
