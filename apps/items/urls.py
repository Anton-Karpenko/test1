from django.urls import path

from apps.items.api.views import (
    ItemsAPIView,
    RetrieveAPIView,
)

app_name = "items"

urlpatterns = [
    path('', ItemsAPIView.as_view(), name='items'),
    path('<slug:pk>/', RetrieveAPIView.as_view(), name='retrieve_item'),
]
