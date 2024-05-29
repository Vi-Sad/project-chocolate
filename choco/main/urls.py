from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main

urlpatterns = [
    path('', main.main, name='main'),
    path('user_active/<slug:name>/<slug:hard_id>/', main.main_user, name='main_user'),
]

handler404 = 'main.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
