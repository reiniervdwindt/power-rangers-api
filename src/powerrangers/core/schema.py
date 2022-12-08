import graphene

import powerrangers.rangers.schema


class Query(
    powerrangers.rangers.schema.Query,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
