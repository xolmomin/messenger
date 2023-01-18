from django.views.generic import TemplateView


#  TODO: Editing later / because i can't add ""Device model"" / users add manually
class UserSignUpView(TemplateView):
    template_name = 'users/auth/signup.html'


class UserSignInView(TemplateView):
    template_name = 'users/auth/signin.html'


class UserResetPasswordView(TemplateView):
    template_name = 'users/auth/reset-password.html'


class UserLockScreenView(TemplateView):
    template_name = 'users/auth/lockscreen.html'
