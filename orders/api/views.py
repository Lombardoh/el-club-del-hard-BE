from types import CoroutineType
from rest_framework import viewsets
from accounts.models import Account
from orders.api.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order, ProductInOrder
from cart.models import Cart

def create_order(account, products_cost, tipo_pago, mp_metadata):
    order = Order.objects.create(
                account=account,
                delivery_address = account.street,
                province = account.province,
                city = account.city,
                postal_code =account.postal_code,
                products_cost = products_cost,
                tipo_pago = tipo_pago,
                mp_metadata = mp_metadata
                )
    return order

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        if request.method == 'POST':
            account = Account.objects.get(email=request.user)
            cart = Cart.objects.filter(account=request.user)
            if(cart):
                total=0
                order = create_order(account, 123, 'transferencia', 'no data')
                for item in cart:
                    ProductInOrder.objects.create(
                        product=item.product,
                        quantity=item.quantity,
                        order = order
                    )
                    total +=item.total()
                order.products_cost = total
                order.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # def mp_payment(request):
    #     pass