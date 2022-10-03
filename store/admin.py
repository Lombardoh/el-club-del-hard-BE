from django.contrib import admin
from store.models import Product, Serial, Category

class SerialInline(admin.TabularInline):
    model = Serial
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProducAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'alt', 'description', 'price', 'image')
    search_fields = ('pk', 'name', 'alt', 'description', 'price', 'image')
    list_filter = ()
    fieldsets = ()
    inlines = [SerialInline]


admin.site.register(Product, ProducAdmin)
admin.site.register(Category, CategoryAdmin)
