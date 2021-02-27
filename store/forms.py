from django.forms import *

from .models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new category...'}),
                     max_length=30)