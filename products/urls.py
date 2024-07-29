from django.urls import include, path
from .views import ColorViewSet, ProductViewSet, SizeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products",ProductViewSet,basename="products")
router.register("sizes",SizeViewSet,basename="sizes")
router.register("colors",ColorViewSet,basename="colors")

urlpatterns = [
    path("",include(router.urls)),
]
