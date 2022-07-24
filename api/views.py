from rest_framework import viewsets
from .serializers import ProductSerializer, WishlistSerializer
from .models import Product, WishList
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# @permission_classes((IsAuthenticated,))
# class WishlistViewSet(viewsets.ModelViewSet):
#     queryset = WishList.objects.all()
#     serializer_class = WishlistSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_wishlist(request):
    user = request.user
    wishlist = WishList.objects.filter(user=user)
    serializer = WishlistSerializer(wishlist, many=True)
    return Response(serializer.data)