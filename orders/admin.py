from django.contrib import admin

from .models import OrderItem
from .models import Cart

admin.site.register(Cart)
admin.site.register(OrderItem)
