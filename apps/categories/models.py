from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.base.utils import custom_uuid
from .managers import CategoryQuerySet


class Category(TimeStampedModel):
    id = models.CharField(
        max_length=11,
        primary_key=True,
        default=custom_uuid,
        editable=False,
    )
    title = models.CharField(
        max_length=255
    )
    category = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        related_name='subcategories',
        blank=True
    )
    description = models.TextField()

    objects = CategoryQuerySet.as_manager()

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
