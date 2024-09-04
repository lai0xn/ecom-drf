from django.contrib import admin

from .models import OrderItem
from .models import Cart
from .models.order import Order

admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
