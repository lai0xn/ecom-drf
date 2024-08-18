from django.contrib.auth import get_user_model
from rest_framework import serializers

from orders.serializers.item import ItemSerializer

from ..models.order import Order


USER_MODEL = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model=Order
        depth=2
        fields = "__all__"

    def get_user(self,obj):
        return {
            "id":obj.user.id,
            "name":obj.user.full_name,
            "email":obj.user.email
        }
