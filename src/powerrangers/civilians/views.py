from rest_framework.viewsets import ModelViewSet

from powerrangers.civilians.models import Civilian
from powerrangers.civilians.serializers import CivilianSerializer


class CivilianModelViewSet(ModelViewSet):
    queryset = Civilian.objects.all()
    serializer_class = CivilianSerializer
