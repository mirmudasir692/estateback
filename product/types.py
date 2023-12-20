import graphene
from .models import Product, ProductImage, ProductVideo
from categories.types import CategoryType
from graphene_django import DjangoObjectType
from graphene_gis.converter import gis_converter


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        fields = ("id", "image")


class ProductVideoType(DjangoObjectType):
    class Meta:
        model = ProductVideo
        fields = ("id", "video")


class ProductType(DjangoObjectType):
    category = CategoryType()
    image = ProductImageType()
    video = ProductVideoType()

    class Meta:
        model = Product
        fields = ("category", "location_cords", "total_area", "available", "price",
                  "discounted_price", "description", "image", "video")
