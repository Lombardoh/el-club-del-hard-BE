from email.policy import default
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    quantity = models.IntegerField(default=0)
    label = models.CharField(max_length=50, blank=True)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name