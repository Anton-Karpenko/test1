from rest_framework import serializers

from apps.categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories_count = serializers.IntegerField(default=0)
    items_count = serializers.IntegerField(default=0)

    class Meta:
        fields = ('id', 'title', 'description', 'category', 'subcategories_count', 'items_count')
        model = Category
