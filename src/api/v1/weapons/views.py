from rest_framework import viewsets

from api.v1.weapons.serializers import WeaponSerializer
from characters.models import Weapon


class WeaponsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing weapons
    """
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
