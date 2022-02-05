import django_filters
from .models import ProductList

class ProductFilter(django_filters.FilterSet):
    email_contains = django_filters.CharFilter(field_name='product_name', lookup_expr='icontains')
    class Meta:
        model = ProductList
        fields = []

