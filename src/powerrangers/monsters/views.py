from rest_framework.viewsets import ModelViewSet

from powerrangers.monsters.models import Monster
from powerrangers.monsters.serializers import MonsterSerializer


class MonsterModelViewSet(ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
