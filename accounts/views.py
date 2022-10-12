from telnetlib import STATUS
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Account
from accounts.serializers import RegistrationSerializer, LoginSerializer, ResetPasswordEmailRequestSerializer
from rest_framework.authtoken.models import Token
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import PasswordResetTokenGenerator


@api_view(['GET'])
def account_available(request, username):
    try:
        Account.objects.get(username=username)
        return Response({'message': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'message': 'El usuario esta disponible'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def email_available(request, email):
    try:
        Account.objects.get(email=email)
        return Response({'message': 'El email ya esta en uso'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'message': 'El email esta disponible'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Usuario creado exitosamente.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            return Response(data)
        else:
            data = serializer.errors 
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'El Usuario ingreso exitosamente.'
            data['username'] = account['username']
            data['token'] = account['token']
            
            return Response(data)
        else:
            data['message'] = 'La combinación email/contraseña es incorrecta.'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

class RequestPasswordResetEmail(generics.GenericAPIView):
  serializer_class = ResetPasswordEmailRequestSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(status=status.HTTP_200_OK)

class PasswordTokenCheckAPI(generics.GenericAPIView):
  def post(self, request, token):
    user = Account.objects.filter(email = request.data['email']).first()
    if PasswordResetTokenGenerator().check_token(user, token) == False:
      return Response(status=status.HTTP_403_FORBIDDEN)  
    else:
      user.set_password(request.data['password'])
      user.save()
      data = {}
      data['token'] = Token.objects.get(user=user).key
      data['username'] = user.username
      return Response(data, status=status.HTTP_200_OK)