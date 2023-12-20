import graphene
from graphene_django import DjangoObjectType
from .query import Query
from .mutations import ProductMutation


class Mutation(graphene.ObjectType):
    get_items = ProductMutation.Field()


schema = graphene.Schema(query=Query)
