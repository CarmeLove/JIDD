from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Category, ProductByWeight, ProductByQuantity, Product, Customer, Order, OrderItem
from .forms import CategoryForm, ProductByWeightForm, ProductByQuantityForm, ProductForm, CustomerForm


def store(request):
    context = {}
    return render(request, 'store.html', context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


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


class ProductByQuantityCreateView(CreateView):
    template_name = 'form_create_product_by_quantity.html'
    form_class = ProductByQuantityForm
    success_url = reverse_lazy('products_by_quantity')


class ProductView(ListView):
    template_name = 'products_other.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'form_create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_other')


class CustomerView(ListView):
    template_name = 'customers.html'
    model = Customer


"""CustomerCreateView is for customer, for now it can reverse customers as for Admin,
    but later it has to be changed and reverse store-site or checkout"""


class CustomerCreateView(CreateView):
    template_name = 'form_create_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers')


class OrderView(ListView):
    template_name = 'orders.html'
    model = Order


class OrderItemView(ListView):
    template_name = 'order_items.html'
    model = OrderItem

