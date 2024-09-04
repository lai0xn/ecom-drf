import requests
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.mixins import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from core.perms import IsAdminOrOwner, IsOwner
from ..serializers.order import OrderSerializer
from ..models.order import Order

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminOrOwner]
    def get_permissions(self):

        print(self.action)
        if self.action == "create":
            permission_classes = [IsAuthenticated]
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminOrOwner]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        items = request.user.cart.items.all()
        if not items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["items"] = [item.id for item in items]
        print(data["items"])
        # Calculate the total price
        price = sum(item.product.price * item.quantity for item in items.all())
        data["price"] = price
        data["user"] = request.user.id
    
        # Use the serializer to validate and save the order
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        request.user.cart.items.clear()
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_admin:
                return Order.objects.all()
            return Order.objects.filter(user=self.request.user)
        return Order.objects.none()



@api_view(["GET"])
def get_wilayas(request):
    url = settings.YALIDINE_BASE_URL +"wilayas/"
    resp = requests.get(url,headers={
        "X-API-ID":settings.YALIDINE_API_ID,
        "X-API-TOKEN":settings.YALIDINE_API_TOKEN
    })
    return Response(data=resp.json(),status=status.HTTP_200_OK)

@api_view(["GET"])
def get_communes(request):
    id = request.GET.get("wilaya_id",None)
    if id is None:
        return Response("You need to provide wilaya_id as a query param",status=status.HTTP_400_BAD_REQUEST)

    url = settings.YALIDINE_BASE_URL +"communes/?wilaya_id="+id

    resp = requests.get(url,headers={
        "X-API-ID":settings.YALIDINE_API_ID,
        "X-API-TOKEN":settings.YALIDINE_API_TOKEN
    })
    return Response(data=resp.json(),status=status.HTTP_200_OK)


@api_view(["GET"])
def get_centers(request):
    wilaya_id = request.GET.get("wilaya_id",None)
    commune_id = request.GET.get("commune_id",None)
    if wilaya_id is None and commune_id is None:
        return Response("You need to provide either wilaya_id or commune_id as a query param",
                        status=status.HTTP_400_BAD_REQUEST)


    url = settings.YALIDINE_BASE_URL +"centers/"
    
    params = {}

    if wilaya_id:
        params["wilaya_id"] = wilaya_id

    if commune_id:
        params["commune_id"] = commune_id

    resp = requests.get(url,headers={
        "X-API-ID":settings.YALIDINE_API_ID,
        "X-API-TOKEN":settings.YALIDINE_API_TOKEN
        },params=params)


    return Response(data=resp.json(),status=status.HTTP_200_OK)



@api_view(["GET"])
def get_fees(request):
    wilaya_id = request.GET.get("wilaya_id",None)

    if wilaya_id is None:
        return Response("You need to provide wilaya_id as a query param",status=status.HTTP_400_BAD_REQUEST)

    url = settings.YALIDINE_BASE_URL +"deliveryfees/"
    
    params = {}

    if wilaya_id:
        params["wilaya_id"] = wilaya_id

    resp = requests.get(url,headers={
        "X-API-ID":settings.YALIDINE_API_ID,
        "X-API-TOKEN":settings.YALIDINE_API_TOKEN
        },params=params)


    return Response(data=resp.json(),status=status.HTTP_200_OK)

