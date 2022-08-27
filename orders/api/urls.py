from django.urls import path, include, re_path
from orders.api.views import OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("order", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]