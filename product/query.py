import graphene
from .types import ProductType, ExtendedProductType
from .models import Product
from django.core.paginator import Paginator


class Query(graphene.ObjectType):
    get_products = graphene.Field(ExtendedProductType, category=graphene.String(default_value=""),
                                  price=graphene.Int(default_value=1),
                                  price_under_range=graphene.Boolean(default_value=False),
                                  page=graphene.Int(default_value=1))

    checkout_product = graphene.Field(ProductType, product_id=graphene.ID())

    def resolve_get_products(self, info, category, price, price_under_range, page=1):
        products = Product.objects.get_recommended_products(category=category, price=price,
                                                            price_under_range=price_under_range)
        products_per_page = 4
        paginator = Paginator(products, products_per_page)
        products_for_page = paginator.get_page(page)
        has_next = products_for_page.has_next()
        has_previous = products_for_page.has_previous()
        total_pages = paginator.num_pages

        """
        response with the relevant information
        """
        return ExtendedProductType(
                products=products_for_page,
                has_next=has_next,
                has_previous=has_previous,
                total_pages=total_pages,
                page=page
            )

    def resolve_checkout_product(self, info, product_id):
        product = Product.objects.checkout_product(product_id)
        return Product
