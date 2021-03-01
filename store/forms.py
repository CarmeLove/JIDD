from django.forms import *

from .models import Category, ProductByWeight, ProductByQuantity, Product, Customer


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new category...'}),
                     validators=[capitalized_validator],
                     max_length=30)


class ProductByWeightForm(ModelForm):
    class Meta:
        model = ProductByWeight
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new product...'}),
                     validators=[capitalized_validator],
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
                     validators=[capitalized_validator],
                     max_length=70)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name of new product...'}),
                     validators=[capitalized_validator],
                     max_length=70)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Name...'}),
                     validators=[capitalized_validator],
                     max_length=70)
    email = EmailField(widget=EmailInput(attrs={'placeholder': 'Email...'}),
                       max_length=40)

