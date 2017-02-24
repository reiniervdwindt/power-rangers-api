from rest_framework import serializers

from api.v1.allies.serializers import AllyListSerializer
from api.v1.civilians.serializers import CivilianListSerializer
from api.v1.monsters.serializers import MonsterListSerializer
from api.v1.rangers.serializers import RangerListSerializer
from api.v1.villains.serializers import VillainListSerializer
from series.models import Episode, Series


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'number', 'name', 'imdb_id', 'trakt_id',)
        model = Episode


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)
    allies = AllyListSerializer(many=True)
    civilians = CivilianListSerializer(many=True)
    monsters = MonsterListSerializer(many=True)
    rangers = RangerListSerializer(many=True, source='ranger_set')
    villains = VillainListSerializer(many=True)

    class Meta(object):
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
    allies = AllyListSerializer(many=True)
    civilians = CivilianListSerializer(many=True)
    monsters = MonsterListSerializer(many=True)
    rangers = RangerListSerializer(many=True, source='ranger_set')
    villains = VillainListSerializer(many=True)

    class Meta(object):
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


class SeriesListSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)

    class Meta(object):
        fields = (
            'id',
            'number',
            'name',
            'year',
            'seasons',
        )
        model = Series
