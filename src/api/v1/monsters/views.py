from rest_framework import viewsets

from api.v1.monsters.serializers import MonsterSerializer
from characters.models import Monster


class MonsterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing monsters
    """
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
