from rest_framework import viewsets

from api.v1.rangers.serializers import RangerSerializer
from characters.models import Ranger


class RangersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing rangers
    """
    queryset = Ranger.objects.all()
    serializer_class = RangerSerializer
