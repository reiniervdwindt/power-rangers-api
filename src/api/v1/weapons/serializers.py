from rest_framework import serializers

from weapons.models import Weapon


class WeaponDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type', 'parts')
        model = Weapon


class WeaponListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type',)
        model = Weapon
