from rest_framework import viewsets

from .models import Ad
from .serializers import AdSerializer


class AdViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод обьявлений."""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
