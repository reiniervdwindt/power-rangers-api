from rest_framework import serializers

from powerrangers.weapons.models import Weapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category', 'parts')
        model = Weapon
