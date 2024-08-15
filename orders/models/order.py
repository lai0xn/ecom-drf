from django.contrib.auth import get_user_model
from django.db import models

from .items import OrderItem

USER_MODEL = get_user_model()

STATE = {"delivered":"delivered","pending":"pending","confirmed":"confirmed","shipping":"shipping","canceled":"canceled","ordered":"ordered"}

class Order(models.Model):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    delivered = models.BooleanField(default=False)
    user = models.ForeignKey(USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    price = models.IntegerField(default=0)
    state = models.CharField(max_length=10,choices=STATE)
    created = models.DateTimeField(auto_now_add=True)


