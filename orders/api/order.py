from rest_framework import status, viewsets
from rest_framework.mixins import Response
from rest_framework.permissions import IsAuthenticated
from core.perms import IsAdminOrOwner, IsOwner
from ..serializers.order import OrderSerializer
from ..models.order import Order

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminOrOwner]
    def get_permissions(self):

        if self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminOrOwner]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        items = request.user.cart.items
        request.data["items"] = items
        serializer = OrderSerializer(data=request.data)
        serializer.save(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
