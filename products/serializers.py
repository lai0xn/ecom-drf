from rest_framework import serializers
from .models import Media, Product, Review,Size,Color


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

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    review_set = ReviewSeralizer(many=True,required=False,read_only=True)
    media_set = MediaSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = Product
        fields="__all__"

    

    def get_rating(self,obj):
        rating = 0
        enteries = 0
        for review in obj.review_set.all():
            rating+=review.stars
            enteries+=1

        if enteries!=0:
            return rating/enteries
        return 0

