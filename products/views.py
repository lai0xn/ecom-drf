from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import ColorSerializer, ProductSerializer, ReviewSeralizer, SizeSerializer
from core.perms import IsAdminOrReadOnly
from .models import Color, Product, Review, Size
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

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSeralizer
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
