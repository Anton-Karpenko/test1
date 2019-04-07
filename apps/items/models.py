from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.base.utils import custom_uuid


class Item(TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    title = models.CharField(
        max_length=255
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        related_name='items'
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='items'
    )
    description = models.TextField()
    image = models.OneToOneField(
        'images.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    views_count = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.title
