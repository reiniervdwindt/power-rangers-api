from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.villains.serializers import (VillainDetailSerializer,
                                         VillainListSerializer)
from villains.models import Villain


class VillainDetailView(RetrieveAPIView):
    queryset = Villain.objects.all()
    serializer_class = VillainDetailSerializer


class VillainListView(ListAPIView):
    queryset = Villain.objects.all()
    serializer_class = VillainListSerializer
