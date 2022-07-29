from rest_framework import serializers
from accounts.models import Wishlist, ProductInWishlist
from store.api.serializers import ProductSerializer
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'price', 'image', 'description', 'label')

class ProductInWishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = ProductInWishlist
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'