from django.views.generic import TemplateView


#  TODO: Editing later / because i can't add ""Devise model"" / users add manually
class AuthUserSignUpView(TemplateView):
    template_name = 'users/auth/signup.html'


class AuthUserSignInView(TemplateView):
    template_name = 'users/auth/signin.html'
