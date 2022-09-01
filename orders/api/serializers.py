from enum import unique
from rest_framework import serializers
from orders.models import Order, ProductInOrder
from store.api.serializers import ProductSerializer

class ProductInOrderSerializer(serializers.ModelSerializer):   
    class Meta:
        model = ProductInOrder
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Order
        fields = '__all__'
