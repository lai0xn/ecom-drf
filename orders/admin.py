from django.contrib import admin

from orders.models.items import OrderItem
from .models import Cart

admin.site.register(Cart)
admin.site.register(OrderItem)
