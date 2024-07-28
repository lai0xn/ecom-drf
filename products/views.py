from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
