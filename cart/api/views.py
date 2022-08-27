from rest_framework import viewsets
from cart.api.seiralizers import CartSerializer
from rest_framework.response import Response
from cart.models import Cart
from store.models import Product
from rest_framework import status

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request):
        cart = Cart.objects.filter(account=request.user)
        cart_total = 0
        for item in cart:
            cart_total += item.quantity * item.product.price
        serializer = self.get_serializer(cart, many=True)
        data = ({'cart_total': cart_total}, {'cart' : serializer.data})
        return Response(data, status=status.HTTP_200_OK)
        

    def create(self, request):
        product = Product.objects.get(id = request.data['product']) 
        quantity = request.data['quantity']
        try:
            cart = Cart.objects.get(product=product, account=request.user)
            cart.quantity += int(quantity)
            if cart.quantity < 1 or quantity == 0:
                cart.delete()
                return Response({'message': 'El producto fue eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
            else:
                cart.save()
                return Response({'message': 'El carrito fue modificado con exito'}, status=200)
        except:
            new_cart = Cart(account=request.user, product=product, quantity=request.data['quantity'])
            new_cart.save()
            return Response({'message': 'producto agregado al carrito'}, status=201)

