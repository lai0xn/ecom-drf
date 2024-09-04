from django.contrib.auth import get_user_model
from rest_framework import serializers

from orders.serializers.item import ItemSerializer

from ..models.order import Order
from ..models.items import OrderItem


USER_MODEL = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()
    items = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(), many=True,write_only=True)
    items_data = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(),write_only=True)
    class Meta:
        model=Order
        depth=2
        fields = "__all__"

    def get_user_data(self,obj):
        return {
            "id":obj.user.id,
            "name":obj.user.full_name,
            "email":obj.user.email
        }

    def get_items_data(self,obj):
        serializer = ItemSerializer(obj.items,many=True)
        return serializer.data
