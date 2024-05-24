from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import main.views as main

urlpatterns = [
    path('', main.main, name='main'),
    path('user_active/<slug:name>/<slug:hard_id>/', main.main_user, name='main_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)