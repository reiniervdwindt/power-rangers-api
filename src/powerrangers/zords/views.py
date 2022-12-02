from rest_framework.viewsets import ModelViewSet

from powerrangers.zords.models import Zord
from powerrangers.zords.serializers import ZordSerializer


class ZordModelViewSet(ModelViewSet):
    queryset = Zord.objects.all()
    serializer_class = ZordSerializer
