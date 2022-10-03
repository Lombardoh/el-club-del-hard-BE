from store.models import Product
from store.api.serializers import ProductSerializer
from rest_framework import viewsets

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