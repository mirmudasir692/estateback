from itertools import groupby
from django.contrib.gis.db import models as GeoModels
from django.db import models
from django.db.models import Q
from graphql import GraphQLError
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from categories.models import Category


class ProductImage(models.Model):
    image = ProcessedImageField(
        upload_to='product_images/',
        processors=[ResizeToFill(1024, 1024)],
        format='JPEG',
        options={'quality': 100}
    )


class ProductVideo(models.Model):
    video = models.FileField(upload_to="product_videos")


class ProductManager(models.Manager):

    def get_recommended_products(self, category_id=0, price=0, price_under_range=False):
        filters = Q(available=True)

        if category_id and category_id != 0:
            filters &= Q(category__id=category_id)

        if price_under_range and price != 0:
            filters &= Q(price__lt=price)
        elif price != 0:
            filters &= Q(price__gt=price)

        products = self.filter(filters).only(
            "id", "price", "total_area", "cover_image", "available", "discounted_price"
        ).prefetch_related("image", "video")

        return products

    def get_products_for_home(self, category=""):
        products = self.only("id", "cover_image").filter(Q(category__title=category.title()) if category != "" else Q(),
                                                         cover_image__isnull=False)[:12]

        return products

    def checkout_product(self, product_id=None):
        """if not product_id raise error"""

        if not product_id:
            raise GraphQLError(message="please provide provide id")

        product = self.get(id=product_id).select_related("category").prefetch_related("image", "video")
        return product

    def get_products_by_category(self):

        # Retrieve products from the database, ordered by category

        products = self.select_related("category").order_by("category__title")

        # Group products by category using itertools.groupby
        grouped_products = [{'category': key, 'products': list(group)} for key, group in
                            groupby(products, key=lambda x: x.category.title if x.category else None)]

        return grouped_products


class Product(models.Model):
    """
    this is the product model, which will represent the item which we will sell
    """
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="cat_products")
    location_cords = GeoModels.PointField(null=True)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_default=0.0)
    discounted_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, null=True)
    image = models.ManyToManyField(ProductImage, related_name="products")
    video = models.ManyToManyField(ProductVideo, related_name="products")
    cover_image = models.ImageField(upload_to="covers", null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True)
    address = models.CharField(null=True)

    objects = ProductManager()

    def __str__(self):
        return f"product {self.id}"
