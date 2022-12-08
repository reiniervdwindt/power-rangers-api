from rest_framework import serializers

from powerrangers.rangers.models import Ranger
from powerrangers.zords.models import Mode, Zord


class ZordModeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description',)
        model = Mode


class ZordRangerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'color',)
        model = Ranger


class SubZordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'category',)
        model = Zord


class ZordSerializer(serializers.ModelSerializer):
    parts = SubZordSerializer(many=True)
    modes = ZordModeSerializer(many=True)
    pilots = ZordRangerSerializer(many=True)

    class Meta:
        fields = ('id', 'name', 'description', 'category', 'modes', 'parts', 'pilots',)
        model = Zord
