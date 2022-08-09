from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from accounts.api.views import WishlistViewSet #update_wishlist#, get_wishlist

router = routers.DefaultRouter()
router.register("wishlist", WishlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("wishlist/<int:pk>", update_wishlist, name="update_wishlist"),
]

