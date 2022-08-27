from enum import unique
from rest_framework import serializers
from cart.models import Cart
from store.api.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):   
    product = ProductSerializer()
    product_total = serializers.SerializerMethodField('get_product_total')

    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'product_total']

    def get_product_total(self, obj):
        total = 0
        total = total + int(obj.quantity) * float(obj.product.price)
        return total