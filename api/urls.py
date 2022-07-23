from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProductViewSet, WishlistViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("wishlists", WishlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]