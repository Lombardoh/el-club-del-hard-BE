from django.contrib import admin
from django.contrib import admin
from orders.models import Order, ProductInOrder

class ProductInline(admin.TabularInline):
	model = ProductInOrder

class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['id',]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'delivery_address']
    inlines = [ProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)