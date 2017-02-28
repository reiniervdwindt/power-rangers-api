from rest_framework.generics import ListAPIView, RetrieveAPIView

from allies.models import Ally
from api.v1.allies.serializers import AllyDetailSerializer, AllyListSerializer


class AllyDetailView(RetrieveAPIView):
    queryset = Ally.objects.all()
    serializer_class = AllyDetailSerializer


class AllyListView(ListAPIView):
    queryset = Ally.objects.all()
    serializer_class = AllyListSerializer
