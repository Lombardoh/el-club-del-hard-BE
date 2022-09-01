from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'street', 'phone_number', 'city', 'postal_code', 'province', 'neighborhood']