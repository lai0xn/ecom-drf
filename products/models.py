from django.db import models

# Create your models here.

class Size(models.Model):
    size = models.CharField(max_length=10)
   
class Color(models.Model):
    color = models.CharField(max_length=10)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sizes = models.ManyToManyField(Size,null=True,blank=True)
    colors = models.ManyToManyField(Color,null=True,blank=True)
    Price = models.IntegerField(null=False)
