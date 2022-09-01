from statistics import mode
from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.
class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='order_account')
    # amount = models.IntegerField()
    delivery_address = models.TextField(max_length=150)
    province = models.TextField(max_length=70)
    city = models.TextField(max_length=70)
    timestamp = models.DateTimeField(auto_now_add=True)
    postal_code = models.IntegerField()
    products_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.TextField(max_length=30)
    mp_metadata = models.JSONField(null=True)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order_product')
    quantity = models.IntegerField(default=1)