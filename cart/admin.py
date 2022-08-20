from django.contrib import admin
from cart.models import Cart

# class productInCartADmin(admin.ModelAdmin):
#     pass

# class productInCartInline(admin.TabularInline):
#     model = productInCart
#     extra = 0

class cartAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    search_fields = ('pk',)
    list_filter = ()
    fieldsets = ()

# admin.site.register(productInCart, productInCartADmin)
admin.site.register(Cart, cartAdmin)