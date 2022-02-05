from django import forms
from .models import ProductCategory, ProductList, FileUpload, SendFeedback, Order
from django.forms import ModelForm

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductListForm(ModelForm):
    class Meta:
        model = ProductList
        fields = '__all__'

class FileForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'

class FeedbackForm(ModelForm):
    class Meta:
        model = SendFeedback
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']



