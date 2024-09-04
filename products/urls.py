from django.urls import include, path

from products.views import add_email
from .views import ColorViewSet, MediaViewSet, ProductViewSet, ReviewViewSet, SizeViewSet, add_to_wishlist, get_wishlist, remove_from_wishlist
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products",ProductViewSet,basename="products")
router.register("sizes",SizeViewSet,basename="sizes")
router.register("colors",ColorViewSet,basename="colors")
router.register("reviews",ReviewViewSet,basename="reviews")
router.register("media",MediaViewSet,basename="media")

urlpatterns = [
    path("",include(router.urls)),
    path("wishlist/add/<int:id>",add_to_wishlist,name="add-wishlist"),
    path("wishlist/remove/<int:id>",remove_from_wishlist,name="remove-wishlist"),
    path("wishlist",get_wishlist,name="get-wishlist"),
    path("mail/add",add_email,name="add-email")
]
