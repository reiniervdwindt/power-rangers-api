from rest_framework import serializers

from series.models import Series


class SeasonSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'number', 'name', 'year',)
        model = Series


class SeriesSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)

    class Meta(object):
        fields = ('id', 'number', 'name', 'year', 'seasons',)
        model = Series
