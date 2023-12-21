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
        fields = ("id", "category", "location_cords", "total_area", "available", "price",
                  "discounted_price", "description", "image", "video", "cover_image")


class ExtendedProductType(graphene.ObjectType):
    products = graphene.List(ProductType)
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    total_pages = graphene.Int()
    page = graphene.Int()
