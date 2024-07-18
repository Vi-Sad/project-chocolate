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
    # path('logout/', TemplateView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', users.logout, name='logout'),
    # path('account/', users.AccountView.as_view(), name='account'),
    path('account/', users.account, name='account'),
    path('chocolate/id_product=<int:id>/', users.info_product, name='info_product'),
    path('chocolate/favourites/', users.view_favourites, name='favourites'),
    path('chocolate/basket/', users.view_basket, name='basket'),
    path('chocolate/basket/add/id_product=<int:id>/', users.add_basket, name='add_basket'),
    path('chocolate/favourites/add/id_product=<int:id>/',
         users.add_favourites, name='add_favourites'),
    path('chocolate/basket/delete/id_product=<int:id>/',
         users.delete_basket, name='delete_basket'),
    path('chocolate/favourites/delete/id_product=<int:id>/',
         users.delete_favourites, name='delete_favourites'),
    path('feedback/id_product=<int:id>/', users.send_feedback, name='send_feedback'),
    path('account/delete/', users.account_delete, name='account_delete'),
    path('new_password/', users.new_password, name='new_password'),
    path('new_password/check/', users.new_password_check, name='new_password_check'),
    path('update_password/<slug:hard_id>/', users.update_password, name='update_password'),
    path('update_password/check/<slug:hard_id>/', users.update_password_check, name='update_password_check'),
    path('change_password/', users.change_password, name='change_password'),
    path('change_password/check/', users.change_password_check, name='change_password_check'),
    path('cookies/set/', users.cookie_set, name='cookie_set'),
    path('cookies/get/', users.cookie_get, name='cookie_get'),
    path('chocolate/create/', users.create_chocolate, name='create_chocolate'),
    path('chocolate/create/check/', users.create_chocolate_check, name='create_chocolate_check'),
    path('chocolate/orders/', users.orders, name='orders'),
]

handler404 = 'main.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
