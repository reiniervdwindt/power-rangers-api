from rest_framework.viewsets import ModelViewSet

from powerrangers.rangers.models import Ranger
from powerrangers.rangers.serializers import RangerSerializer


class RangerModelViewSet(ModelViewSet):
    queryset = Ranger.objects.all()
    serializer_class = RangerSerializer
