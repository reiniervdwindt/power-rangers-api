from rest_framework import serializers

from characters.models import Villain
from series.models import Series


class VillainSeriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name')

    class Meta(object):
        fields = ('id', 'name',)
        model = Series


class VillainSerializer(serializers.ModelSerializer):
    series = VillainSeriesSerializer(many=True)

    class Meta(object):
        fields = ('id', 'name', 'description', 'gender', 'type', 'homeworld', 'series',)
        model = Villain
