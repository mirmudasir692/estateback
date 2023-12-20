from .models import Category
from graphene_django import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "title", "image")
