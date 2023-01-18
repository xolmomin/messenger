from django.urls import path

from users.views import IndexView, ChatDirectView, ChatGroupView, NewChatView, UserSignUpView, UserSignInView, UserResetPasswordView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat', ChatDirectView.as_view(), name='chat_direct'),
    path('group', ChatGroupView.as_view(), name='chat_group'),
    path('new/chat', NewChatView.as_view(), name='new_chat'),
    path('auth/signup/', UserSignUpView.as_view(), name='auth_signup'),
    path('auth/signin/', UserSignInView.as_view(), name='auth_signin'),
    path('auth/reset-password/', UserResetPasswordView.as_view(), name='reset_password')
]
