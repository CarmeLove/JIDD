from django.contrib import admin

from .models import Category, ProductByWeight, ProductByQuantity, Product

admin.site.register(Category)
admin.site.register(ProductByWeight)
admin.site.register(ProductByQuantity)
admin.site.register(Product)