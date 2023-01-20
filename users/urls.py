from django.urls import path

from users.views import SignUpFormView, IndexView, ChatDirectView, ChatGroupView, NewChatView, UserSignInView, \
    UserResetPasswordView, UserLockScreenView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat', ChatDirectView.as_view(), name='chat_direct'),
    path('group', ChatGroupView.as_view(), name='chat_group'),
    path('new/chat', NewChatView.as_view(), name='new_chat'),
    path('auth/signup/', SignUpFormView.as_view(), name='auth_signup'),
    path('auth/signin/', UserSignInView.as_view(), name='auth_signin'),
    path('auth/reset-password/', UserResetPasswordView.as_view(), name='reset_password'),
    path('auth/lockscreen/', UserLockScreenView.as_view(), name='auth_lockscreen'),
]
