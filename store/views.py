from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Category, ProductByWeight, ProductByQuantity
from .forms import CategoryForm, ProductByWeightForm, ProductByQuantityForm


class CategoryView(ListView):
    template_name = 'categories.html'
    model = Category


class CategoryCreateView(CreateView):
    template_name = 'form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('create_category')


class ProductByWeightView(ListView):
    template_name = 'products_by_weight.html'
    model = ProductByWeight


class ProductByWeightCreateView(CreateView):
    template_name = 'form_create_product_by_weight.html'
    form_class = ProductByWeightForm
    success_url = reverse_lazy('products_by_weight')


class ProductByQuantityView(ListView):
    template_name = 'products_by_quantity.html'
    model = ProductByQuantity