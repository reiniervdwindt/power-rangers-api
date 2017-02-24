from rest_framework import serializers

from civilians.models import Civilian


class CivilianDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'nickname', 'description',)
        model = Civilian


class CivilianListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'nickname', 'description',)
        model = Civilian
