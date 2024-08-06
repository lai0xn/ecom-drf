from rest_framework import serializers

from orders.models.cart import Cart
from .item import ItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def get_items(self,obj):
        return obj.items.all()
