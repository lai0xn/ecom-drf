from rest_framework import serializers

from ..models.items import OrderItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
