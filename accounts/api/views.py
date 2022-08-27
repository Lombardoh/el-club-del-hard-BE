from rest_framework import viewsets
from accounts.models import Account
from accounts.api.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
import json

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request):
        account = Account.objects.get(id=request.user.id)
        serializer = AccountSerializer(account)
        data = serializer.data
        
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        print(request.data['data'])
        if request.method == 'PUT':
            serializer = AccountSerializer(request.data['data'])
            data = serializer.data
            try:
                Account.objects.filter(id=request.user.id).update(**data)
                return Response({'message':'Usuario actualizado con exito'}, status=status.HTTP_200_OK)
            except:
                return Response({'message':'Hubo un error al actualizar el usuario'}, status=status.HTTP_400_BAD_REQUEST)

           
            
          
                
                


               
        

