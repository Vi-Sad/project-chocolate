from django.urls import include, path
from django.conf import settings
import users.views as users
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('registration/', users.Registration.as_view(), name='registration'),
    path('registration/check/', users.registration_check, name='registration_check'),
    path('login/', users.Login.as_view(), name='login'),
    path('login/check', users.login_check, name='login_check'),
    path('logout/', TemplateView.as_view(template_name='users/logout.html'), name='logout'),
    path('account/<slug:name>/<slug:hard_id>/', users.AccountView.as_view(), name='account'),
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
    path('new_password/', users.new_password, name='new_password'),
    path('new_password/check/', users.new_password_check, name='new_password_check'),
    path('update_password/<slug:hard_id>/', users.update_password, name='update_password'),
    path('update_password/check/<slug:hard_id>/', users.update_password_check, name='update_password_check'),
]

handler404 = 'main.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
