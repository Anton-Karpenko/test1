from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.items.models import Item
from apps.items.services import increment_views_count
from .serializers import ItemSerializer
from .filters import ItemsFilter


class ItemsAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().prefetch_related('image')
    permission_classes = IsAuthenticatedOrReadOnly,
    filter_class = ItemsFilter


class RetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance = increment_views_count(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
