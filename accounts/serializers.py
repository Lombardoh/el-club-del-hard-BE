from rest_framework import serializers
from accounts.models import Account
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwards = {'password': {'write_only': True}}

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        account.set_password(password)
        account.save()

        return account

class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')
        
        self.context['user'] = user
        
        return data
    
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        data = {
            'token': token.key,
            'username': self.context['user'].username
        }
        return data