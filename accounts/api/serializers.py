from rest_framework import serializers
from accounts.models import Wishlist, ProductInWishlist
from store.api.serializers import ProductSerializer
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'price', 'image', 'description')

class ProductInWishlistSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=False)
    class Meta:
        model = ProductInWishlist
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    products = ProductInWishlistSerializer(many=True, read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'products']