
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import WishList
from accounts.api.serializers import WishlistSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from accounts.models import Account

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer

@api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
def get_wishlist(request, token):
    user = Token.objects.get(key=token).user
    account = Account.objects.get(email=user)
    wishlist = WishList.objects.get(account=account)
    serializer = WishlistSerializer(wishlist, many=True)
    return Response(serializer.data)

    