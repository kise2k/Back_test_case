from rest_framework import serializers

from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор для модели добавления объявлений."""

    class Meta:
        model = Ad
        fields = (
            'id',
            'title',
            'views',
            'author',
            'position'
        )

