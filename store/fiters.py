import django_filters
from .models import *


class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    price = django_filters.RangeFilter()

    class Meta:
        model = Products
        fields = ['name', 'price', 'status']


