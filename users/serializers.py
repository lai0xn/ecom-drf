from django.contrib.auth import get_user_model
from django.contrib.auth.models import make_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ["email","password","full_name"]
    def create(self, validated_data):
        userModel = get_user_model()
        print(validated_data)
        user = userModel.objects.create_user(**validated_data)
        return user
        
    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
