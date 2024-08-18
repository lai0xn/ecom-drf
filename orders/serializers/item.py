from rest_framework import serializers
from products.serializers import ProductSerializer, SizeSerializer,ColorSerializer
from ..models.items import OrderItem


class ItemSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=False)
    color = ColorSerializer(many=False)
    product = serializers.SerializerMethodField()        
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_product(self,obj):
        return {
            "id":obj.product.id,
            "title":obj.product.title,
            "price":obj.product.price,
            "media":[media.image.url for media in obj.product.media_set.all() if media.primary],
        }
