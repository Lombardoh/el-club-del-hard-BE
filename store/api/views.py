from store.models import Product, Category
from store.api.serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

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