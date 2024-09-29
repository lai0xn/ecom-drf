from django.urls import include, path

from products.views import add_email
from .views import ColorViewSet, CouponViewSet, MediaViewSet, ProductViewSet, ReviewViewSet, SizeViewSet, add_to_wishlist, check_coupon, get_wishlist, remove_from_wishlist,get_recommended
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products",ProductViewSet,basename="products")
router.register("sizes",SizeViewSet,basename="sizes")
router.register("colors",ColorViewSet,basename="colors")
router.register("reviews",ReviewViewSet,basename="reviews")
router.register("media",MediaViewSet,basename="media")
router.register("coupons",CouponViewSet,basename="coupons")
urlpatterns = [
    path("",include(router.urls)),
    path("wishlist/add/<int:id>",add_to_wishlist,name="add-wishlist"),
    path("wishlist/remove/<int:id>",remove_from_wishlist,name="remove-wishlist"),
    path("products/recommendations",get_recommended,name="recommendations"),
    path("wishlist",get_wishlist,name="get-wishlist"),
    path("coupons/check",check_coupon,name="check-coupon"),
    path("mail/add",add_email,name="add-email")
]
