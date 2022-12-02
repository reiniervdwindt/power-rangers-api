from rest_framework import serializers

from powerrangers.civilians.models import Civilian


class CivilianSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'nickname', 'description',)
        model = Civilian
