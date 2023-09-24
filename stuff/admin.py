from django.contrib import admin
from .models import Product, comment,Cart, CartItem
# Register your models here.

class CommentInline(admin.TabularInline):
    model = comment
    
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_display = ['name','id','price']
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product','id']

admin.site.register(Product,ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart)



