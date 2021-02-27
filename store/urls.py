from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='create_category'),
    path('products/by_weight/', ProductByWeightView.as_view(), name='products_by_weight'),
    path('products/by_weight/create/', ProductByWeightCreateView.as_view(), name='create_product_by_weight'),
]