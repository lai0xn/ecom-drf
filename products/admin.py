from django.contrib import admin

from .models import Color, Media, Product, Review, Size


admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Review)
admin.site.register(Media)
admin.site.register(Size)
