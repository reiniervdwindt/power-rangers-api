from rest_framework import serializers

from characters.models import Ranger, Zord, ZordMode


class ZordModeSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = ZordMode


class ZordRangerSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'color',)
        model = Ranger


class SubZordSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description', 'type',)
        model = Zord


class ZordSerializer(serializers.ModelSerializer):
    parts = SubZordSerializer(many=True)
    modes = ZordModeSerializer(many=True)
    pilots = ZordRangerSerializer(many=True)

    class Meta(object):
        fields = ('id', 'name', 'description', 'type', 'modes', 'parts', 'pilots',)
        model = Zord
