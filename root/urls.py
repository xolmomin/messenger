from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root import settings

urlpatterns = [
    path('', include('users.urls')),
    path('chats/', include('chats.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
