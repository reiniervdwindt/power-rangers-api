from rest_framework import serializers

from characters.models import Ally


class AllySerializer(serializers.ModelSerializer):
    class Meta(object):
        fields = ('id', 'name', 'description',)
        model = Ally
