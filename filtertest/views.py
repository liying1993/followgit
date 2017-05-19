from django.shortcuts import render
from filtertest.models import *
# Create your views here.
import django_filters
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model=Product
        fields = ['price','release_date']