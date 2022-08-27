from enum import unique
from rest_framework import serializers
from orders.models import Order, ProductInOrder
from store.api.serializers import ProductSerializer

class ProductInOrderSerializer(serializers.ModelSerializer):   
    class Meta:
        model = ProductInOrder
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):   
    # product = ProductSerializer()
    # product_in_order = ProductInOrderSerializer()
    # product_total = serializers.SerializerMethodField('get_product_total')

    class Meta:
        model = Order
        fields = '__all__'

    # def get_product_total(self, obj):
    #     total = 0
    #     total = total + int(obj.quantity) * float(obj.product.price)
    #     return total