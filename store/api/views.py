from store.models import Product, Category
from store.api.serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  pagination_class = None

  def update(self, request, pk):
    print(request.data['action'], pk, request.user.is_admin)
    if(not request.user.is_admin):
      return Response(status=status.HTTP_401_UNAUTHORIZED)
    if(request.data['action'] == 'add'):
      Category.objects.get(id=pk).products.add(Product.objects.get(id = request.data['product']))
      return Response({'message': 'El producto fue agregado con exito'}, status=status.HTTP_200_OK)
    else:
      Category.objects.get(id=pk).products.remove(Product.objects.get(id = request.data['product']))
      return Response({'message': 'El producto fue removido con exito'}, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def get_queryset(self):
    name = self.request.query_params.get('q')
    if(name):
      queryset = Product.objects.filter(name__icontains = name)
    else:
      queryset = Product.objects.all()
    return queryset