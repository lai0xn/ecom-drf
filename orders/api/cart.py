from django.core.serializers import serialize
from django.db.models import query
from rest_framework.decorators import api_view,permission_classes
from rest_framework.mixins import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404
from ..models.cart import Cart
from ..models.items import OrderItem
from ..serializers.cart import CartSerializer
from products.models import Product

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_current_cart(request):
    serializer = CartSerializer(request.user.cart,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request,id):
    cart = request.user.cart
    product = Product.objects.get(id=id)
    
    size = request.data.get("size",None)
    color = request.data.get("color",None)
    quantity = request.data.get("quantity",1)
    item_q = OrderItem.objects.filter(
        cart=cart,
        product=product,
        size=size,
        color=color,
    )


    if item_q.exists():
        item = item_q[0]
        item.quantity+=quantity
        item.save()
        
        product.in_stock -= quantity
        product.save()
        return Response("Increased quantity",status=status.HTTP_200_OK)
    
    OrderItem.objects.create(
        product=product,
        cart=cart,
        quantity=quantity,
        color=color,
        size=size 
    )

    
    product.in_stock -= quantity
    product.save()


    return Response("Proruct added to cart",status=status.HTTP_200_OK)


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








