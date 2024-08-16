from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

CATEGORIES = {"Abaya":"Abaya","Planner":"Planner"}


USER_MODEL = get_user_model()

class Size(models.Model):
    size = models.CharField(max_length=10)
   
class Color(models.Model):
    color = models.CharField(max_length=10)




class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=15,choices=CATEGORIES,default="Abaya")
    sizes = models.ManyToManyField(Size,null=True,blank=True)
    colors = models.ManyToManyField(Color,null=True,blank=True)
    price = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    in_stock = models.IntegerField(default=1,null=False)


class Media(models.Model):
    image = models.ImageField(upload_to="products")
    primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stars = models.IntegerField()
    content = models.TextField()
