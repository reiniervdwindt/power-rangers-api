from rest_framework import serializers

from series.models import Episode, Series


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'number', 'name', 'imdb_id', 'trakt_id',)
        model = Episode


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta(object):
        fields = ('id', 'number', 'name', 'year', 'imdb_id', 'trakt_id', 'episodes',)
        model = Series


class SeriesSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)
    episodes = EpisodeSerializer(many=True)

    class Meta(object):
        fields = ('id', 'number', 'name', 'year', 'seasons', 'episodes',)
        model = Series
