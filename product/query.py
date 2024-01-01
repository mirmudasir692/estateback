import graphene
from django.core.paginator import Paginator
from categories.models import Category
from categories.types import CategoryType
from .models import Product
from .types import ProductType, ExtendedProductType


class Query(graphene.ObjectType):
    get_categories = graphene.List(CategoryType)  # get the categories with their products

    get_products = graphene.Field(ExtendedProductType, category_id=graphene.ID(default_value=0),
                                  price=graphene.Float(default_value=1),
                                  price_under_range=graphene.Boolean(default_value=False),
                                  page=graphene.Int(default_value=1))
    get_products_for_home = graphene.List(ProductType, category=graphene.String())

    checkout_product = graphene.Field(ProductType, product_id=graphene.ID())

    def resolve_get_products_for_home(self, info, category=0):
        products = Product.objects.get_products_for_home(category)
        print(products)
        return products

    def resolve_get_products(self, info, category_id, price, price_under_range, page=1):
        products = Product.objects.get_recommended_products(category_id=category_id, price=price,
                                                            price_under_range=price_under_range)
        print(category_id, price_under_range)
        products_per_page = 9
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
        print(product_id)
        product = Product.objects.checkout_product(product_id)
        print(product)
        return product

    def resolve_get_categories(self, info):
        categories = Category.objects.get_categories()
        return categories
