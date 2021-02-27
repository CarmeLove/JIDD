from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Category, ProductByWeight
from .forms import CategoryForm


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