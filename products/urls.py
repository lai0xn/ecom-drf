from django.urls import include, path
from .views import ColorViewSet, MediaViewSet, ProductViewSet, ReviewViewSet, SizeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products",ProductViewSet,basename="products")
router.register("sizes",SizeViewSet,basename="sizes")
router.register("colors",ColorViewSet,basename="colors")
router.register("reviews",ReviewViewSet,basename="reviews")
router.register("media",MediaViewSet,basename="media")

urlpatterns = [
    path("",include(router.urls)),
]
