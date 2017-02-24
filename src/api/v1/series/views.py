from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.series.serializers import (SeriesDetailSerializer,
                                       SeriesListSerializer)
from series.models import Series


class SeriesDetailView(RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesDetailSerializer


class SeriesListView(ListAPIView):
    queryset = Series.objects.filter(parent__isnull=True)
    serializer_class = SeriesListSerializer
