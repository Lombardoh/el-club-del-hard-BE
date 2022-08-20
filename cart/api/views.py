from rest_framework import viewsets
from accounts.models import Account
from cart.api.seiralizers import CartSerializer, CartUserSerializer
from rest_framework.response import Response
from cart.models import Cart

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartUserViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartUserSerializer

    def retrieve(self, request, pk=None):
        account = Account.objects.get(pk=pk)
        cart = Cart.objects.filter(account=account)
        serializer = CartUserSerializer(cart, many=True)
        print('retrieve', pk, account)
       
        return Response(serializer.data)
