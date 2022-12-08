from rest_framework import serializers

from powerrangers.rangers.models import Appearance, Ranger
from powerrangers.weapons.models import Weapon
from powerrangers.zords.models import Zord


class RangerWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category',)
        model = Weapon


class RangerZordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'category',)
        model = Zord


class AppearanceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='series')
    weapon = RangerWeaponSerializer()
    zord = RangerZordSerializer()

    class Meta:
        fields = ('name', 'weapon', 'zord',)
        model = Appearance


class RangerSerializer(serializers.ModelSerializer):
    series = AppearanceSerializer(source='appearance_set', many=True)

    class Meta:
        fields = ('id', 'name', 'color', 'series',)
        model = Ranger
