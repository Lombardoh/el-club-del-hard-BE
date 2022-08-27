from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from accounts.api.views import AccountViewSet

router = routers.DefaultRouter()
router.register("accounts", AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

