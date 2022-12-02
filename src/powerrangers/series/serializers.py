from rest_framework import serializers

from powerrangers.allies.serializers import AllySerializer
from powerrangers.civilians.serializers import CivilianSerializer
from powerrangers.monsters.serializers import MonsterSerializer
from powerrangers.rangers.serializers import RangerSerializer
from powerrangers.series.models import Episode, Series
from powerrangers.villains.serializers import VillainSerializer


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'number', 'name', 'imdb_id', 'trakt_id',)
        model = Episode


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)
    allies = AllySerializer(many=True)
    civilians = CivilianSerializer(many=True)
    monsters = MonsterSerializer(many=True)
    rangers = RangerSerializer(many=True, source='ranger_set')
    villains = VillainSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'year',
            'imdb_id',
            'trakt_id',
            'episodes',
            'allies',
            'civilians',
            'monsters',
            'rangers',
            'villains',
        )
        model = Series


class SeriesDetailSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)
    episodes = EpisodeSerializer(many=True)
    allies = AllySerializer(many=True)
    civilians = CivilianSerializer(many=True)
    monsters = MonsterSerializer(many=True)
    rangers = RangerSerializer(many=True, source='ranger_set')
    villains = VillainSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'year',
            'seasons',
            'episodes',
            'allies',
            'civilians',
            'monsters',
            'rangers',
            'villains',
        )
        model = Series
        depth = 1


class SimpleSeasonSerializer(serializers.ModelSerializer):
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
    seasons = SimpleSeasonSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'year',
            'seasons',
        )
        model = Series
