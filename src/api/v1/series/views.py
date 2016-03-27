from rest_framework import viewsets

from api.v1.series.serializers import SeriesSerializer
from series.models import Series


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing series
    """
    queryset = Series.objects.filter(parent__isnull=True)
    serializer_class = SeriesSerializer
