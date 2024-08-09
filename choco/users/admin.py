from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Basket)
admin.site.register(Feedback)
admin.site.register(Orders)