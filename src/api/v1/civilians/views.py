from rest_framework import viewsets

from api.v1.civilians.serializers import CivilianSerializer
from characters.models import Civilian


class CivilianViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing civilians
    """
    queryset = Civilian.objects.all()
    serializer_class = CivilianSerializer
