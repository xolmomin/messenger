from django.urls import path

from users.views import IndexView, ChatDirectView, ChatGroupView, NewChatView, SignUpGetVerificationFormView, \
    UserSignInView, UserResetPasswordView, SignUpVerifyFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat', ChatDirectView.as_view(), name='chat_direct'),
    path('group', ChatGroupView.as_view(), name='chat_group'),
    path('new/chat', NewChatView.as_view(), name='new_chat'),
    path('auth/signup/', SignUpGetVerificationFormView.as_view(), name='auth_signup'),
    path('auth/signup/verify', SignUpVerifyFormView.as_view(), name='auth_signup_verify'),
    path('auth/signin/', UserSignInView.as_view(), name='auth_signin'),
    path('auth/reset-password/', UserResetPasswordView.as_view(), name='reset_password')
]
