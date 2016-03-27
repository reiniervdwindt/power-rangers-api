from rest_framework import viewsets

from api.v1.villains.serializers import VillainSerializer
from characters.models import Villain


class VillainsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing villains
    """
    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
