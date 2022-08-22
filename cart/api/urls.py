from django.urls import path, include, re_path
from cart.api.views import CartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("cart", CartViewSet)

urlpatterns = [
    path("", include(router.urls)),
]