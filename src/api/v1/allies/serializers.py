from rest_framework import serializers

from allies.models import Ally


class AllyDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Ally


class AllyListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Ally
