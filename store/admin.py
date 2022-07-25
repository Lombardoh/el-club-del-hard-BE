from django.contrib import admin
from store.models import Product

class ProducAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'alt', 'description', 'price', 'image')
    search_fields = ('pk', 'name', 'alt', 'description', 'price', 'image')
    list_filter = ()
    fieldsets = ()


admin.site.register(Product, ProducAdmin)
