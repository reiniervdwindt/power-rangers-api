from rest_framework import serializers

from rangers.models import Appearance, Ranger
from weapons.models import Weapon
from zords.models import Zord


class RangerWeaponSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type',)
        model = Weapon


class RangerZordSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type',)
        model = Zord


class SeriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='series')
    weapon = RangerWeaponSerializer()
    zord = RangerZordSerializer()

    class Meta(object):
        fields = ('name', 'weapon', 'zord',)
        model = Appearance


class RangerDetailSerializer(serializers.ModelSerializer):
    series = SeriesSerializer(source='appearance_set', many=True)

    class Meta(object):
        fields = ('id', 'name', 'color', 'series',)
        model = Ranger


class RangerListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'color',)
        model = Ranger
