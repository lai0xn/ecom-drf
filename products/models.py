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
    Category = models.CharField(max_length=15,choices=CATEGORIES,default="Abaya")
    sizes = models.ManyToManyField(Size,null=True,blank=True)
    colors = models.ManyToManyField(Color,null=True,blank=True)
    Price = models.IntegerField(null=False)


class Review(models.Model):
    user = models.ForeignKey(USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    stars = models.IntegerField()
    content = models.TextField()
