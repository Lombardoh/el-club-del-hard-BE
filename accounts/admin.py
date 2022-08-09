from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account, Wishlist
from store.models import Product

class ProductInline(admin.TabularInline):
	model = Product

class AccountAdmin(UserAdmin):
	list_display = ('pk', 'email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('pk', 'email','username',)
	readonly_fields=('pk', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class WishlistAdmin(admin.ModelAdmin):
	list_display = ('pk',)
	inlines = [ProductInline]
	

admin.site.register(Account, AccountAdmin)
admin.site.register(Wishlist, WishlistAdmin)