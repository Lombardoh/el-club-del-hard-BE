from django.contrib import admin
from store.models import Product, Serial, Category
from import_export.admin import ImportExportModelAdmin

class SerialInline(admin.TabularInline):
  model = Serial
  extra = 0

class CategoryAdmin(admin.ModelAdmin):
  pass

class ProducAdmin(ImportExportModelAdmin):
  list_display = ('pk', 'name', 'alt', 'description', 'price', 'image')
  search_fields = ('pk', 'name', 'alt', 'description', 'price', 'image')
  ordering = ('name',)
  list_filter = ()
  fieldsets = ()
  inlines = [SerialInline]


admin.site.register(Product, ProducAdmin)
admin.site.register(Category, CategoryAdmin)
