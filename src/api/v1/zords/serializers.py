from rest_framework import serializers

from rangers.models import Ranger
from zords.models import Mode, Zord


class ZordModeSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Mode


class ZordRangerSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'color',)
        model = Ranger


class SubZordSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description', 'type',)
        model = Zord


class ZordDetailSerializer(serializers.ModelSerializer):
    parts = SubZordSerializer(many=True)
    modes = ZordModeSerializer(many=True)
    pilots = ZordRangerSerializer(many=True)

    class Meta(object):
        fields = ('id', 'name', 'description', 'type', 'modes', 'parts', 'pilots',)
        model = Zord


class ZordListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description', 'type',)
        model = Zord
