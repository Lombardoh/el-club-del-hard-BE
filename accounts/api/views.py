from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import Wishlist
from accounts.api.serializers import WishlistSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from accounts.models import Account

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    # @api_view(['PUT'])
    # def update(self, request, *args, **kwargs):
    #     print("pkaaaaaaaaaaaaaaaa")
    #     wishlist = Wishlist.objects.get(id=8)
    #     serializer = WishlistSerializer(wishlist, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    # @api_view(['GET', ])
    # # @permission_classes((IsAuthenticated,))
    # def show(request, token):
    #     print("get")
    #     user = Token.objects.get(key=token).user
    #     account = Account.objects.get(email=user)
    #     wishlist = Wishlist.objects.get(account=account)
    #     serializer = WishlistSerializer(wishlist, many=False)
    #     print(serializer.data)
    #     return Response(serializer.data)

    