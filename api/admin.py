from atexit import register
from django.contrib import admin
from api.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'alt', 'description', 'price', 'image')
    search_fields = ('pk', 'name', 'alt', 'description', 'price', 'image')

   
admin.site.register(Product, ProductAdmin)