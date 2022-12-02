from rest_framework import serializers

from powerrangers.monsters.models import Monster


class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description',)
        model = Monster
