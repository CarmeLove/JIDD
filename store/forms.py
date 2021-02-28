from django.forms import *

from .models import Category, ProductByWeight, ProductByQuantity, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new category...'}),
                     max_length=30)


class ProductByWeightForm(ModelForm):
    class Meta:
        model = ProductByWeight
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new product...'}),
                     max_length=70)
#     category = ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
#     price = DecimalField
#     availability = FloatField(null=False, blank=False)
#     weight = FloatField(null=True, blank=True)
#     image = ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name


class ProductByQuantityForm(ModelForm):
    class Meta:
        model = ProductByQuantity
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new product...'}),
                     max_length=70)
