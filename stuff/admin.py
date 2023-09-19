from django.contrib import admin
from .models import Product, comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = comment
    
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_display = ['name','id','price']
    

admin.site.register(Product,ProductAdmin)


