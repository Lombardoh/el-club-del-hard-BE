from django.contrib import admin
from store.models import Product, Serial

class SerialInline(admin.TabularInline):
    model = Serial
    extra = 0

class ProducAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'alt', 'description', 'price', 'image')
    search_fields = ('pk', 'name', 'alt', 'description', 'price', 'image')
    list_filter = ()
    fieldsets = ()
    inlines = [SerialInline]


admin.site.register(Product, ProducAdmin)
