from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import users.views as users
from django.views.generic import TemplateView

urlpatterns = [
    path('registration/', TemplateView.as_view(template_name='users/registration.html'), name='registration'),
    path('registration/check/', users.registration_check, name='registration_check'),
    path('login/', TemplateView.as_view(template_name='users/login.html'), name='login'),
    path('login/check', users.login_check, name='login_check'),
    path('logout/', users.logout, name='logout'),
    path('account/<slug:name>/<slug:hard_id>/', users.account, name='account'),
    path('chocolate/id_product=<int:id>/', users.info_product, name='info_product'),
    path('chocolate/<slug:name>/favourites/<slug:hard_id>/', users.view_favourites, name='favourites'),
    path('chocolate/<slug:name>/basket/<slug:hard_id>/', users.view_basket, name='basket'),
    path('chocolate/<slug:name>/basket/add/id_product=<int:id>/<slug:hard_id>/', users.add_basket, name='add_basket'),
    path('chocolate/<slug:name>/favourites/add/id_product=<int:id>/<slug:hard_id>/',
         users.add_favourites, name='add_favourites'),
    path('chocolate/<slug:name>/basket/delete/id_product=<int:id>/<slug:hard_id>/',
         users.delete_basket, name='delete_basket'),
    path('feedback/<slug:name>/id_product=<int:id>/<slug:hard_id>/', users.send_feedback, name='send_feedback'),
    path('account/<slug:name>/delete/<slug:hard_id>/', users.account_delete, name='account_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
