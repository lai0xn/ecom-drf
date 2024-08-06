from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import ColorSerializer, ProductSerializer, SizeSerializer
from core.perms import IsAdminOrReadOnly
from .models import Color, Product, Size
# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()


class SizeViewSet(ModelViewSet):
    serializer_class = SizeSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Size.objects.all()



class ColorViewSet(ModelViewSet):
    serializer_class =  ColorSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Color.objects.all()
