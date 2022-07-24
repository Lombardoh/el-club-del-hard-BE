from django.db import models
from accounts.models import Account

class Product(models.Model):
    name = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

class WishList(models.Model):
    account = models.ForeignKey(Account, related_name='wishlist', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)