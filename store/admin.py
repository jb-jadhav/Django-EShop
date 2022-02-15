from django.contrib import admin

from .models.category import Category
from .models.product import Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','description','image']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
