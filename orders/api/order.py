from rest_framework import status, viewsets
from rest_framework.mixins import Response
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
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminOrOwner]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        items = request.user.cart.items
        if not items.exists():
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["items"] = list(items.values_list('id', flat=True))
    
        # Calculate the total price
        price = sum(item.product.price * item.quantity for item in items.all())
        data["price"] = price
        data["user"] = request.user.id
    
        # Use the serializer to validate and save the order
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        items.update(cart=None)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
