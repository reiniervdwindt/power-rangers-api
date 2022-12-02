from rest_framework import serializers

from powerrangers.allies.models import Ally


class AllySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description',)
        model = Ally
