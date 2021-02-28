from django.db.models import CharField, Model, DecimalField, ImageField, FloatField, ForeignKey, SET_NULL, IntegerField, \
    BooleanField


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductByWeight(Model):
    class Meta:
        verbose_name = 'Product By Weight'
        verbose_name_plural = 'Products By Weight'

    name = CharField(max_length=70)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    price = DecimalField(max_digits=6, decimal_places=2)
    availability = FloatField(null=False, blank=False)
    weight = FloatField(null=True, blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductByQuantity(Model):
    class Meta:
        verbose_name = 'Product By Quantity'
        verbose_name_plural = 'Products By Quantity'

    name = CharField(max_length=70)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    price = DecimalField(max_digits=6, decimal_places=2)
    availability = IntegerField(null=False, blank=False)
    weight = FloatField(null=True, blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = CharField(max_length=70)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    price = DecimalField(max_digits=6, decimal_places=2)
    availability = IntegerField(null=False, blank=False)
    weight = FloatField(null=True, blank=True)
    digital = BooleanField(default=False, null=True, blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name