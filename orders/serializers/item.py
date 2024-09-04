from rest_framework import serializers
from products.serializers import ProductSerializer, SizeSerializer,ColorSerializer
from ..models.items import OrderItem


class ItemSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=False)
    color = ColorSerializer(many=False)
    product = ProductSerializer(many=False,read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

