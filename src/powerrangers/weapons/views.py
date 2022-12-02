from rest_framework.viewsets import ModelViewSet

from powerrangers.weapons.models import Weapon
from powerrangers.weapons.serializers import WeaponSerializer


class WeaponModelViewSet(ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
