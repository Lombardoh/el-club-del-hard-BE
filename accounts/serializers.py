import os
from rest_framework import serializers
from accounts.models import Account
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail

SITE_URL = str(os.getenv("SITE_URL"))

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
            'username': self.context['user'].username,
            'is_admin': self.context['user'].is_admin
        }
        return data

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
  email = serializers.EmailField(min_length=10)

  class Meta:
    fields = ['email']

  def validate(self, data):
    try:
      email=data['email']
      user = Account.objects.get(email=email)
      token = PasswordResetTokenGenerator().make_token(user)
      if Account.objects.filter(email=email).exists():        
        reset_url = SITE_URL + 'password-reset/?token=' + token
        body = """Se ha solicitado un recupero de contraseña para tu cuenta.\n
        Para cambiar tu contraseña has click en el siguiente link: \n
        {} \n
        Si no fuiste tu por favor ignora este correo.""".format(reset_url)
        send_mail(
                'Recupera tu contraseña',
                body,
                'clubdelhard@reply.com',
                [email],
                fail_silently=False,
            )
      return data
    except:
      pass
    return super().validate(data)