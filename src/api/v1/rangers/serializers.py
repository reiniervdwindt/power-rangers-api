from rest_framework import serializers

from characters.models import Ranger, Weapon, Zord


class RangerWeaponSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type',)
        model = Weapon


class RangerZordSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'type',)
        model = Zord


class RangerSerializer(serializers.ModelSerializer):
    weapon = RangerWeaponSerializer()
    zords = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:v1:zord-detail'
    )

    class Meta(object):
        fields = ('id', 'name', 'color', 'weapon', 'zords',)
        model = Ranger
