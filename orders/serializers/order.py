from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models.order import Order


USER_MODEL = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = "__all__"
