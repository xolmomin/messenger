from django.urls import path

from users.views import UserSignUpView, UserSignInView, UserResetPasswordView

urlpatterns = [
    path('auth/signup/', UserSignUpView.as_view(), name='auth_signup'),
    path('auth/signin/', UserSignInView.as_view(), name='auth_signin'),
    path('auth/reset-password/', UserResetPasswordView.as_view(), name='reset_password')
]
