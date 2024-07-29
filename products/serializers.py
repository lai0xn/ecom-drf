from rest_framework import serializers
from .models import Product,Size,Color

class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields="__all__"

    def get_sizes(self,obj):
        return obj.sizes.all()
    
    def get_colors(self,obj):
        return obj.colors.all()



class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields="__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields="__all__"
