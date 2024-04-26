from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import users.views as users

urlpatterns = [
    path('registration/', users.registration, name='registration'),
    path('registration/check/', users.registration_check, name='registration_check'),
    path('login/', users.login, name='login'),
    path('login/check', users.login_check, name='login_check'),
    path('account/<slug:name>/', users.account, name='account')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
