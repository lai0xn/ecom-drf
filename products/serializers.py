from rest_framework import serializers
from .models import Product, Review,Size,Color

class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields="__all__"

    def get_sizes(self,obj):
        return obj.sizes.all()
    
    def get_colors(self,obj):
        return obj.colors.all()


    def get_reviews(self,obj):
        return obj.review_set.all()



class ReviewSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields="__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields="__all__"
