from rest_framework import serializers

from characters.models import Civilian


class CivilianSerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'nickname', 'description',)
        model = Civilian
