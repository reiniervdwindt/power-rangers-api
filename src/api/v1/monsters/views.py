from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.monsters.serializers import (MonsterDetailSerializer,
                                         MonsterListSerializer)
from monsters.models import Monster


class MonsterDetailView(RetrieveAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterDetailSerializer


class MonsterListView(ListAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterListSerializer
