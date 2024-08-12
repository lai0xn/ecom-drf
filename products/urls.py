from django.urls import include, path
from .views import ColorViewSet, ProductViewSet, ReviewViewSet, SizeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products",ProductViewSet,basename="products")
router.register("sizes",SizeViewSet,basename="sizes")
router.register("colors",ColorViewSet,basename="colors")
router.register("reviews",ReviewViewSet,basename="reviews")
urlpatterns = [
    path("",include(router.urls)),
]
