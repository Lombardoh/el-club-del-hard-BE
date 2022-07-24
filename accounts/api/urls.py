from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from accounts.api.views import WishlistViewSet, get_wishlist

router = routers.DefaultRouter()
router.register("wishlist", WishlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("wishlist/<str:token>", get_wishlist, name="get_wishlist"),
]

