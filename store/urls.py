from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='create_category'),
    path('products/by_weight/', ProductByWeightView.as_view(), name='products_by_weight'),
    path('products/by_weight/create/', ProductByWeightCreateView.as_view(), name='create_product_by_weight'),
    path('products/by_quantity/', ProductByQuantityView.as_view(), name='products_by_quantity'),
    path('products/by_quantity/create/', ProductByQuantityCreateView.as_view(), name='create_product_by_quantity'),
    path('products/other/', ProductView.as_view(), name='products_other'),
    path('products/other/create/', ProductCreateView.as_view(), name='create_products_other'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('create_account/', CustomerCreateView.as_view(), name='create_customer'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('orders/<pk>/items/', OrderItemView.as_view(), name='order_items'),
]