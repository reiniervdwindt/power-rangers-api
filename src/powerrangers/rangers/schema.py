import graphene
from graphene_django import DjangoObjectType

from powerrangers.rangers.models import Ranger


class RangerType(DjangoObjectType):
    class Meta:
        model = Ranger
        fields = ('id', 'name', 'color')


class Query(graphene.ObjectType):
    rangers = graphene.List(RangerType)

    def resolve_rangers(self, info):
        return Ranger.objects.all()
