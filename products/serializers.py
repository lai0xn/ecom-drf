from rest_framework import serializers

from users.models import Email, User
from users.serializers import UserSerializer
from .models import Media, Product, Review,Size,Color, WishList


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
    colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(),many=True,write_only=True)
    sizes = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all(),many=True,write_only=True)
    colors_data = serializers.SerializerMethodField()
    sizes_data = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields="__all__"

    def get_colors_data(self,obj):
        serializer = ColorSerializer(obj.colors,many=True)
        return serializer.data
        

    def get_sizes_data(self,obj):
        serializer = SizeSerializer(obj.sizes,many=True)
        return serializer.data

    

    def get_rating(self,obj):
        rating = 0
        enteries = 0
        for review in obj.review_set.all():
            rating+=review.stars
            enteries+=1

        if enteries!=0:
            return rating/enteries
        return 0



class WishListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = WishList
        fields = "__all__"

    def get_user(self,obj):
        return {
            "id":obj.user.id,
            "name":obj.user.full_name,
            "email":obj.user.email
        }


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
