from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import cart as cart_view
from .api import order as order_view


router = DefaultRouter()

router.register("orders",order_view.OrderView,basename="orders")

urlpatterns = [
    path("cart/add-to-cart/<int:id>",cart_view.add_to_cart,name="add-to-cart"),
    path("cart",cart_view.get_current_cart,name="cart"),
    path("cart/remove-from-cart/<int:id>",cart_view.remove_from_cart,name="remove-from-cart"),
    path("",include(router.urls))

]
