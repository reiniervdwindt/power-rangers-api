from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from powerrangers.core.mixins import MultiSerializerViewSetMixin
from powerrangers.series.models import Episode, Series
from powerrangers.series.serializers import EpisodeSerializer, SeasonSerializer, SeriesSerializer


class SeriesModelViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Series.objects.series()
    serializer_class = SeriesSerializer
    serializer_classes = {
        'retrieve': SeriesSerializer,
        'list': SeriesSerializer,
        'seasons': SeasonSerializer,
        'episodes': EpisodeSerializer,
    }

    @action(detail=True)
    def seasons(self, request, pk=None):
        series = self.get_object()
        seasons = series.seasons.filter(parent__pk=pk)
        serializer = self.get_serializer_class()(seasons, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def episodes(self, request, pk=None):
        season = self.get_object()
        episodes = season.episodes.all()
        serializer = self.get_serializer_class()(episodes, many=True)
        return Response(serializer.data)


class SeasonModelViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Series.objects.seasons()
    serializer_class = SeasonSerializer
    serializer_classes = {
        'retrieve': SeasonSerializer,
        'list': SeasonSerializer,
        'episodes': EpisodeSerializer,
    }

    @action(detail=True)
    def episodes(self, request, pk=None, series_pk=None):
        season = self.get_object()
        episodes = season.episodes.filter(series__pk=pk)
        serializer = self.get_serializer_class()(episodes, many=True)
        return Response(serializer.data)


class EpisodeModelViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    serializer_classes = {
        'retrieve': EpisodeSerializer,
        'list': EpisodeSerializer,
    }
