from django.urls import path

from users.views.auth import AuthUserSignUpView, AuthUserSignInView

urlpatterns = [
    path('auth/signup/', AuthUserSignUpView.as_view(), name='auth_signup'),
    path('auth/signin/', AuthUserSignInView.as_view(), name='auth_signin')
]
