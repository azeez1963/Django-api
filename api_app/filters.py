import django_filters
from .models import Product


class ProductFilter(django_filters.Filter):
    product_name=django_filters.CharFilter(look_expr='icontains')
    price=django_filters.NumberFilter(lookup_expr='gte')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Product
        fields =['product_name', 'description', 'price', 'discount_price', 'category', 'expire_date', 'production_date', 'product_img', 'rating']
        