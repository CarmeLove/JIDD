from django.contrib.auth.models import User
from django.db.models import CharField, Model, DecimalField, ImageField, FloatField, ForeignKey, SET_NULL, IntegerField, \
    BooleanField, OneToOneField, CASCADE, DateTimeField, F


class Customer(Model):
    user = OneToOneField(User, null=True, blank=True, on_delete=CASCADE)
    name = CharField(max_length=70, null=True)
    email = CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


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

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    customer = ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True)
    date_ordered = DateTimeField(auto_now_add=True)
    complete = BooleanField(default=False, null=True, blank=False)
    transaction_id = IntegerField()

    def __str__(self):
        return str(self.id)

    @property
    def transaction_counter(self):
        transaction_id = Order.objects.all()
        transaction_id.update(stories_filed=F('stories_filed') + 1)
        return transaction_id


"""
FOR NOW OrderItem just for ProductByWeight.
Have to find solution to add different products and kinds of quantities."""


class OrderItem(Model):
    product_by_weight = ForeignKey(ProductByWeight, on_delete=SET_NULL, null=True, blank=True)
    order = ForeignKey(Order, on_delete=SET_NULL, null=True, blank=True)
    quantity = FloatField(default=0, null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product_by_weight.price * self.quantity
        return total
