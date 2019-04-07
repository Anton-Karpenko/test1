from rest_framework import serializers

from apps.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'original_image', 'preview_image', 'created')
