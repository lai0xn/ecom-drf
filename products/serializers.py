from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer
from .models import Media, Product, Review,Size,Color


class ReviewSeralizer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    class Meta:
        model = Review
        fields = '__all__'

    def get_user_detail(self,obj):
        serializer = UserSerializer(obj.user,many=False)
        return serializer.data
        
         


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

