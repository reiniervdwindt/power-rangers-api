from rest_framework import serializers

from powerrangers.series.models import Series
from powerrangers.villains.models import Villain


class VillainSeriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        fields = ('id', 'name',)
        model = Series


class VillainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'gender', 'type', 'homeworld',)
        model = Villain
