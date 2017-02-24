from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.zords.serializers import ZordDetailSerializer, ZordListSerializer
from zords.models import Zord


class ZordDetailView(RetrieveAPIView):
    queryset = Zord.objects.all()
    serializer_class = ZordDetailSerializer


class ZordListView(ListAPIView):
    queryset = Zord.objects.all()
    serializer_class = ZordListSerializer
