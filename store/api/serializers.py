from itertools import product
from rest_framework import serializers
from store.models import Product, Serial, Category

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['pk', 'name', 'alt', 'description', 'price', 'image', 'quantity', 'label', 'discount']

class CategorySerializer(serializers.ModelSerializer):
  products = ProductSerializer(read_only=True, many=True)
  class Meta:
      model = Category
      fields = '__all__'
