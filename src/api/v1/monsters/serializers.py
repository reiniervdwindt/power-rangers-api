from rest_framework import serializers

from characters.models import Monster


class MonsterSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Monster
