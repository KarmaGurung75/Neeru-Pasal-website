from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User

# Model For Product Category
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_info = models.TextField()
    category_image = models.FileField(upload_to='static/category_uploads', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

# Model For Product List
class ProductList(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_image = models.FileField(upload_to='static/product_uploads')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name

# Model For Gallery
class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='static/uploads')

# Model For Contact Feedback
class SendFeedback(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(null=True, validators=[validate_email])
    subject = models.CharField(max_length=10)
    message = models.CharField(max_length=200)

# Model For Cart
class Cart(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

# Model For Wishlist
class Wishlist(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Model For Product Ordering
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
    )
    product = models.ForeignKey(ProductList, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    payment_method = models.CharField(max_length=200, choices=PAYMENT, null=True)
    payment_status = models.BooleanField(default=False, null=True, blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    contact_address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)