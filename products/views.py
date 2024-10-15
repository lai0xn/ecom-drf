from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import Email
from .serializers import ColorSerializer, CouponSerializer, MailSerializer, MediaSerializer, ProductSerializer, ReviewSeralizer, SizeSerializer, WishListSerializer
from core.perms import IsAdminOrReadOnly, OwnerOrReadOnly
from .models import Color, Coupon, Media, Product, Review, Size, WishList
# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()


class CouponViewSet(ModelViewSet):
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]
    queryset = Coupon.objects.all()

class SizeViewSet(ModelViewSet):
    serializer_class = SizeSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Size.objects.all()


class MediaViewSet(ModelViewSet):
    serializer_class = MediaSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Media.objects.all()


class ColorViewSet(ModelViewSet):
    serializer_class =  ColorSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Color.objects.all()

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSeralizer
    permission_classes = [OwnerOrReadOnly]
    queryset = Review.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, id):
    # Get or create the wishlist for the current user
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    
    # Get the product or return a 404 response if not found
    product = get_object_or_404(Product, id=id)
    
    # Add the product to the wishlist
    if product not in wishlist.products.all():
        wishlist.products.add(product)
        return Response({"message": "Product added to wishlist"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Product already in wishlist"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request,id):
    wishlist = get_object_or_404(WishList,user=request.user)
    product = get_object_or_404(Product,id=id)
    wishlist.products.remove(product)
    return Response("Product remove from wishlist",status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_wishlist(request):
    wishlist = get_object_or_404(WishList,user=request.user)
    serializer = WishListSerializer(wishlist,many=False)
    return Response(data=serializer.data,status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_emails(request):
    emails = Email.objects.all()
    serializer = MailSerializer(emails,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def check_coupon(request):
    coupon = request.data.get("coupon",None)
    if coupon == None:
        return Response("no coupon provided",status=status.HTTP_400_BAD_REQUEST)
    coupon_model = get_object_or_404(Coupon,name=coupon)
    serializer = CouponSerializer(coupon_model,many=False)
    return Response(data=serializer.data,status=status.HTTP_200_OK)




@api_view(["POST"])
def add_email(request):
    serializer = MailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(["GET"])
def get_recommended(request):
    number = int(request.GET.get("number", 0))  # Default to 0 if 'number' is not provided
    products = Product.objects.order_by('-id')  # Get products in reverse order by id
    if number > 0 and number < products.count():
        products = products[:number]  # Slice the QuerySet correctly from the beginning
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
