from django.contrib import admin
from .models import Product, comment
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id','price']
    

admin.site.register(Product,ProductAdmin)
admin.site.register(comment)

