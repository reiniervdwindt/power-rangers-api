from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.rangers.serializers import (RangerDetailSerializer,
                                        RangerListSerializer)
from rangers.models import Ranger


class RangerDetailView(RetrieveAPIView):
    queryset = Ranger.objects.all()
    serializer_class = RangerDetailSerializer


class RangerListView(ListAPIView):
    queryset = Ranger.objects.all()
    serializer_class = RangerListSerializer
