from django.views.generic import ListView

from .models import Category


class CategoryView(ListView):
    template_name = 'categories.html'
    model = Category
