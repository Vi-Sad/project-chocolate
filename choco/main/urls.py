from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main

urlpatterns = [
    # path('', main.MainView.as_view(), name='main'),
    path('', main.main, name='main'),
    path('logout/', main.logout, name='logout'),
    path('about_us/', main.about_us, name='about_us'),
]

handler404 = 'main.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
