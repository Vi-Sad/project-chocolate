from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import users.views as users

urlpatterns = [
    path('registration/', users.registration, name='registration'),
    path('registration/check/', users.registration_check, name='registration_check'),
    path('login/', users.login, name='login'),
    path('login/check', users.login_check, name='login_check'),
    path('logout/', users.logout, name='logout'),
    path('account/<slug:name>/', users.account, name='account'),
    path('chocolate/id_product=<int:id>/', users.info_product, name='info_product'),
    path('chocolate/<slug:name>/favourites/', users.view_favourites, name='favourites'),
    path('chocolate/<slug:name>/basket/', users.view_basket, name='basket'),
    path('chocolate/<slug:name>/basket/add/id_product=<int:id>/', users.add_basket, name='add_basket'),
    path('chocolate/<slug:name>/favourites/add/id_product=<int:id>/', users.add_favourites, name='add_favourites'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
