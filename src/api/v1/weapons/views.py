from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.weapons.serializers import (WeaponDetailSerializer,
                                        WeaponListSerializer)
from weapons.models import Weapon


class WeaponDetailView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponDetailSerializer


class WeaponListView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponListSerializer
