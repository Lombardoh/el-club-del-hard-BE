from itertools import product
from django.db import models
from accounts.models import Account
from store.models import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='cart_product')
    quantity = models.IntegerField(default=1)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cart_account')

    def total(self):
        return self.quantity * self.product.price