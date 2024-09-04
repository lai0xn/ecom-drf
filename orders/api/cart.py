from rest_framework.decorators import api_view,permission_classes
from rest_framework.mixins import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from ..serializers.cart import CartSerializer
from products.models import Color, Product,Size
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..models import Cart,OrderItem
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_current_cart(request):
    serializer = CartSerializer(request.user.cart,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request, id):
    cart = request.user.cart
    
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    size_id = request.data.get("size", None)
    color_id = request.data.get("color", None)
    quantity = request.data.get("quantity", 1)
    custom_text = request.data.get("custom_text",None)
    try:
        quantity = int(quantity)
        if quantity <= 0:
            return Response({"error": "Quantity must be a positive integer"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)

       
    size = None
    color = None

    if size_id:
        size = get_object_or_404(Size,id=size_id)
    
    if color_id:
        color = get_object_or_404(Color,id=color_id)

    item_q = OrderItem.objects.filter(
        cart=cart,
        product=product,
        size=size,
        color=color,
        custom_text=custom_text
    )

    with transaction.atomic():
        if item_q.exists():
            item = item_q.first()
            item.quantity += quantity
            item.save()
            message = "Increased quantity"
        else:
            OrderItem.objects.create(
                product=product,
                cart=cart,
                quantity=quantity,
                color=color,
                size=size,
                custom_text=custom_text
            )
            message = "Product added to cart"


    return Response(message, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request,id):
    cart = request.user.cart
    
    order_item = get_object_or_404(OrderItem, id=id, cart=cart)
    
    order_item.delete()

    return Response("Proruct deleted from cart",status=status.HTTP_200_OK) 


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def decrease_quantity(request,id):
    cart = request.user.cart
    product = Product.objects.get(id=id)

    size = request.data.get("size",None)
    color = request.data.get("color",None)
    quantity = request.data.get("quantity",1)

    itemq = OrderItem.objects.filter(
        cart=cart,
        product=product,
        size=size,
        color=color
    )
    if len(itemq) == 0:
        return Response("You don't have this product in your cart")
    
    if itemq.exists():
        item = itemq[0]
        item.quantity -= quantity

        item.save()
        

    return Response("Proruct deleted from cart",status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_all_carts(request):
    queryset = Cart.objects.all()
    serializer = CartSerializer(queryset,many=True)
    return Response(serializer.data,status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_cart(request,id):
    queryset = get_object_or_404(Cart,id=id)
    serializer = CartSerializer(queryset,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)








