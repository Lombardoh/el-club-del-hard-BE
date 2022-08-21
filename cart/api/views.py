from hashlib import new
from rest_framework import viewsets
from accounts.models import Account
from cart.api.seiralizers import CartSerializer, CartUserSerializer
from rest_framework.response import Response
from cart.models import Cart
from store.models import Product

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartUserViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartUserSerializer

    def list(self, request):
        cart = Cart.objects.filter(account=request.user)
        print(cart)

        serializer = self.get_serializer(cart, many=True)
        return Response(serializer.data)

    def create(self, request):
        print("create",request.headers['Authorization'])
        product = Product.objects.get(id = request.data['product'])
        new_cart = Cart(account=request.user, product=product, quantity=request.data['quantity'])
        new_cart.save()
        return Response({'message': 'producto agregado al carrito'})

