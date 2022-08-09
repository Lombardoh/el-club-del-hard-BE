from rest_framework import serializers
from accounts.models import Account, Wishlist
from store.api.serializers import ProductSerializer
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    product_id = serializers.RelatedField(source='product', read_only=True)
    class Meta:
        model = Wishlist
        fields = '__all__'
    
    # def get(self, request, *args, **kwargs):
    #     print("get")
    #     user = request.user
    #     wishlist = Wishlist.objects.get(account=user)
    #     serializer = WishlistSerializer(wishlist, many=False)
    #     return serializer.data

    # def create(self, validated_data): 
    #     user = validated_data.pop('account')
    #     try:
    #         Wishlist.objects.get(account=user)
    #     except:
    #         wishlist = Wishlist.objects.create(account=user)
    #         wishlist.save()
    #     return wishlist

    # def update(self, instance, validated_data): 
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance