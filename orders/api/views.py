from rest_framework import viewsets
from orders.api.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from cart.models import Cart

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        if request.method == 'POST':
            cart = Cart.objects.filter(account=request.user)
            print(cart)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # def mp_payment(request):
    #     pass