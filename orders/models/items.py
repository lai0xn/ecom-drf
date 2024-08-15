from django.db import models

from products.models import Color, Product, Size
from .cart import Cart

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=0)
    custom_text = models.CharField(max_length=10,null=True)

