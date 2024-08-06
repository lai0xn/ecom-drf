from django.contrib.auth import get_user_model
from django.db import models

from .items import OrderItem

USER_MODEL = get_user_model()

class Order(models.Model):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    delivered = models.BooleanField(default=False)
    user = models.ForeignKey(USER_MODEL,on_delete=models.CASCADE)
    Items = models.ManyToManyField(OrderItem)
