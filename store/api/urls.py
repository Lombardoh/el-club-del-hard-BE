from django.urls import path, include
from rest_framework import routers
from store.api.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]