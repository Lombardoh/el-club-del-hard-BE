from django.contrib import admin
from django.contrib import admin
from orders.models import Order, ProductInOrder

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',]

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['id',]

admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)