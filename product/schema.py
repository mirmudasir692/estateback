import graphene
from graphene_django import DjangoObjectType
from .query import Query


schema = graphene.Schema(query=Query)
