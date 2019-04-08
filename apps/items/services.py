from django.db.models import F

from apps.images.models import Image
from .models import Item


class CreateItem:
    fields = ('owner', 'image')

    def __init__(self, user, validated_data):
        self.owner = user
        self.validated_data = validated_data

    def create(self):
        for x in self.fields:
            getattr(self, f'set_{x}')()
        return Item.objects.create(**self.validated_data)

    def set_owner(self):
        self.validated_data.update({'owner': self.owner})

    def set_image(self):
        upload_image = self.validated_data.pop('upload_image', None)
        if upload_image:
            image = Image.objects.create(original_image=upload_image)
            self.validated_data.update({'image': image})


def increment_views_count(instance):
    instance.views_count = F('views_count') + 1
    instance.save()
    instance.refresh_from_db(fields=('views_count',))
    return instance
