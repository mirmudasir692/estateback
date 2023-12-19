from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.gis.db import models as GeoModels
from categories.models import Category, Discount
from imagekit.processors import ResizeToFill


class ProductImage(models.Model):
    image = ProcessedImageField(
        upload_to='product_images/',
        processors=[ResizeToFill(1024, 1024)],
        format='JPEG',
        options={'quality': 100}
    )


class ProductVideo(models.Model):
    video = models.FileField(upload_to="product_videos")


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

    def __str__(self):
        return f"product {self.id}"



