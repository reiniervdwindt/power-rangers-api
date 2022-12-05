from rest_framework import serializers

from powerrangers.series.models import Series, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'imdb_id',
            'trakt_id',
        )
        model = Episode


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'year',
            'imdb_id',
            'trakt_id',
        )
        model = Series


class SeriesSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'year',
            'seasons',
        )
        model = Series
