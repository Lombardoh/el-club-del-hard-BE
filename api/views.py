from rest_framework import viewsets
from .serializers import ProductSerializer, WishlistSerializer
from .models import Product, WishList

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer