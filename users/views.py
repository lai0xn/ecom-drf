import time
from django.contrib.auth import authenticate
from django.shortcuts import render
from drf_spectacular.utils import OpenApiRequest, OpenApiResponse, extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status

from orders.models.order import Order
from users.models import User
from .serializers import LoginSerializer, UserSerializer
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user(request):
    user = request.user
    return Response({
        "name":user.full_name,
        "email":user.email,
        "is_admin":user.is_admin
    },status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def all_users(request):
    serializer = UserSerializer(User.objects.all(),many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_customers(request):
    users = User.objects.filter(order__isnull=False,order__state="delivered").distinct()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_stats(request):
    users_count = len(User.objects.all())
    customer_count = len(User.objects.filter(order__isnull=False,order__state="delivered").distinct())
    total_orders = Order.objects.exclude(state="canceled")
    total_revenue = sum([order.price for order in Order.objects.filter(state="delivered")])
    return Response(data={
        "users_count":users_count,
        "customer_count":customer_count,
        "total_revenue":total_revenue,
        "total_orders":total_orders

    },status=status.HTTP_200_OK)


@extend_schema(
    responses={
    200:UserSerializer,
    },
    request=UserSerializer,
)
@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else :
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@extend_schema(
    responses={
    200:LoginSerializer,
    },
    request=LoginSerializer,
)
@api_view(["POST"])
def login(request):
    start_time = time.time()
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(email=request.data["email"],password=request.data["password"])
    end_time = time.time()  # End the timer

    duration_ms = (end_time - start_time) * 1000
    print(duration_ms)
    if user is None:
        return Response("Invalid Credentials",status=status.HTTP_400_BAD_REQUEST)
    
    token = user.generate_jwt()

    return Response({"token":token},status=status.HTTP_200_OK)
   




