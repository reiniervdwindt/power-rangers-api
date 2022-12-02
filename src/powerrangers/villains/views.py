from rest_framework.viewsets import ModelViewSet

from powerrangers.villains.models import Villain
from powerrangers.villains.serializers import VillainSerializer


class VillainModelViewSet(ModelViewSet):
    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
