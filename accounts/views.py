from telnetlib import STATUS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Account
from accounts.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.authtoken.models import Token

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
            data = serializer.errors 
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)