from django.urls import path

from users.views.auth import AuthUserSignUpView

urlpatterns = [
    path('auth/signup/', AuthUserSignUpView.as_view(), name='auth_signup')
]
