import graphene
from .types import ProductType
from .models import Product


class Query(graphene.ObjectType):
    get_products = graphene.List(ProductType)

    def resolve_get_products(self, info):
        products = Product.objects.all()
        return products
