from rest_framework import serializers

from monsters.models import Monster


class MonsterDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Monster


class MonsterListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Monster
