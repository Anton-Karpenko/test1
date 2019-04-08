from django_filters import rest_framework as filters

from apps.items.models import Item


class ItemsFilter(filters.FilterSet):
    created_after = filters.IsoDateTimeFilter(
        field_name='created',
        lookup_expr='gte',
    )
    owner = filters.CharFilter(
        field_name='owner',
        lookup_expr='exact'
    )
    category = filters.CharFilter(
        field_name='category',
        lookup_expr='exact'
    )
    views_count_greater = filters.NumberFilter(
        field_name='views_count',
        lookup_expr='gte'
    )
    price_less = filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )

    class Meta:
        model = Item
        fields = ('created_after', 'owner', 'category', 'views_count_greater', 'price_less')
