from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.civilians.serializers import (CivilianDetailSerializer,
                                          CivilianListSerializer)
from civilians.models import Civilian


class CivilianDetailView(RetrieveAPIView):
    queryset = Civilian.objects.all()
    serializer_class = CivilianDetailSerializer


class CivilianListView(ListAPIView):
    queryset = Civilian.objects.all()
    serializer_class = CivilianListSerializer
