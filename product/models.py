from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.gis.db import models as GeoModels
from categories.models import Category, Discount
from imagekit.processors import ResizeToFill
from django.db.models import F, Q
from graphql import GraphQLError


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
    def get_recommended_products(self, category="", price=0, price_under_range=False):
        products = self.filter(Q(available=True) &
                               ((Q(category__title=category.title()) if category != "" else Q()) &
                                (Q(price__lt=price) if price_under_range and price != 0 else Q(price__gt=price)
                                 if price != 0 else Q(price__gt=0)
                                 )
                                )).select_related("category").prefetch_related("image", "video")

        return products

    def checkout_product(self, product_id=None):

        """if not product_id raise error"""

        if not product_id:
            raise GraphQLError(message="please provide provide id")

        product = self.get(id=product_id).select_related("category").prefetch_related("image", "video")
        return product


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
    ip_address = models.GenericIPAddressField(null=True)
    address = models.CharField(null=True)

    objects = ProductManager()

    def __str__(self):
        return f"product {self.id}"
