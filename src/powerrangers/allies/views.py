from rest_framework.viewsets import ModelViewSet

from powerrangers.allies.models import Ally
from powerrangers.allies.serializers import AllySerializer


class AllyModelViewSet(ModelViewSet):
    queryset = Ally.objects.all()
    serializer_class = AllySerializer
