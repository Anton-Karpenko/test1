from rest_framework import serializers

from apps.images.api.serializers import ImageSerializer
from apps.items.models import Item
from apps.items.services import CreateItem


class ItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    upload_image = serializers.ImageField(write_only=True, allow_null=True, required=False)

    class Meta:
        fields = ('id', 'title', 'owner', 'category', 'description', 'image', 'views_count', 'upload_image', 'price')
        model = Item
        extra_kwargs = {
            'views_count': {'read_only': True},
            'category': {'required': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        return CreateItem(user, validated_data).create()
