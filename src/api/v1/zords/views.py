from rest_framework import viewsets

from api.v1.zords.serializers import ZordSerializer
from characters.models import Zord


class ZordsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing zords
    """
    queryset = Zord.objects.all()
    serializer_class = ZordSerializer
