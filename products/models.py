from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

CATEGORIES = {"Abaya":"Abaya","Planner":"Planner"}

STOCK = {"available":"available","out of stock":"out of stock","hidden":"hidden"}

USER_MODEL = get_user_model()

class Size(models.Model):
    size = models.CharField(max_length=100)
   
class Color(models.Model):
    color = models.CharField(max_length=100)




class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=15,choices=CATEGORIES,default="Abaya")
    sizes = models.ManyToManyField(Size,null=True,blank=True)
    colors = models.ManyToManyField(Color,null=True,blank=True)
    price = models.IntegerField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    custom_text = models.BooleanField(default=False)
    in_stock = models.CharField(choices=STOCK,max_length=20)


class Media(models.Model):
    image = models.ImageField(upload_to="products")
    primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stars = models.IntegerField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



class WishList(models.Model):
    user = models.OneToOneField(USER_MODEL,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
