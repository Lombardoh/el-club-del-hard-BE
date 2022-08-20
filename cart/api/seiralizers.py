from enum import unique
from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['account', 'products', 'quantity']


class CartUserSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Cart
        fields = ['product', 'quantity']
