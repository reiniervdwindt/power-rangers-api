from rest_framework import viewsets

from api.v1.allies.serializers import AllySerializer
from characters.models import Ally


class AllyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing civilians
    """
    queryset = Ally.objects.all()
    serializer_class = AllySerializer
