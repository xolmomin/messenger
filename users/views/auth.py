from django.views.generic import TemplateView


class AuthUserSignUpView(TemplateView):
    template_name = 'users/auth/signup.html'
