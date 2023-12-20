import graphene
from .types import ProductType
from .models import Product
# from .api import get_address


class Query(graphene.ObjectType):
    get_products = graphene.List(ProductType)

    def resolve_get_products(self, info):
        request = info.context
        # ip_address = request.META.get('REMOTE_ADDR', None)
        # print(ip_address)
        # ip_address = "169.149.195.21"  # this is like placeholder for testing purpose
        # address = get_address(ip_address)
        products = Product.objects.get_recommended_products(price=2000)
        return products
