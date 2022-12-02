from rest_framework.viewsets import ModelViewSet

from powerrangers.series.models import Series
from powerrangers.series.serializers import SeriesSerializer


class SeriesModelViewSet(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
