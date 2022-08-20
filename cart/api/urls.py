from django.urls import path, include, re_path
from cart.api.views import CartViewSet, CartUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cart", CartViewSet)
router.register("cart_user", CartUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]