from django.urls import path

from apps.categories.api.views import (
    CategoryAPIView,
)

app_name = "categories"

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
]
