from django.contrib import admin

from .models import Category, ProductByWeight

admin.site.register(Category)
admin.site.register(ProductByWeight)