from rest_framework import serializers
from store.models import Product, Serial

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'alt', 'description', 'price', 'image', 'quantity', 'label', 'discount']

