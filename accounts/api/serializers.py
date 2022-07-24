from rest_framework import serializers
from accounts.models import WishList

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'