from itertools import product
from django.contrib import admin
from cart.models import Cart

class cartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'quantity', 'product')
    search_fields = ('pk',)
    list_filter = ()
    fieldsets = ()

admin.site.register(Cart, cartAdmin)