from rest_framework import generics

from apps.categories.models import Category
from .serializers import CategorySerializer


class CategoryAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.with_counts()
