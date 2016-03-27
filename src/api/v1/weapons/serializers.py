from rest_framework import serializers

from characters.models import Ranger, Weapon


class WeaponRangerSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'color',)
        model = Ranger


class WeaponSerializer(serializers.ModelSerializer):
    ranger = WeaponRangerSerializer()

    class Meta(object):
        fields = ('id', 'name', 'type', 'ranger',)
        model = Weapon
