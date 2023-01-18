from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'users/index.html'


class ChatDirectView(TemplateView):
    template_name = 'users/chat-direct.html'


class ChatGroupView(TemplateView):
    template_name = 'users/chat-group.html'


class NewChatView(TemplateView):
    template_name = 'users/chat-empty.html'
