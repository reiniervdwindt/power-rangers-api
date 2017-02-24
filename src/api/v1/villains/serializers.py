from rest_framework import serializers

from series.models import Series
from villains.models import Villain


class VillainSeriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta(object):
        fields = ('id', 'name',)
        model = Series


class VillainDetailSerializer(serializers.ModelSerializer):
    series = VillainSeriesSerializer(many=True)

    class Meta(object):
        fields = ('id', 'name', 'description', 'gender', 'type', 'homeworld', 'series',)
        model = Villain


class VillainListSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description', 'gender', 'type', 'homeworld',)
        model = Villain
