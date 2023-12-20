from django.contrib import admin
from .models import Product, ProductImage, ProductVideo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "location_cords", "total_area", "available", "price",
                    "discounted_price",
                    "description", "ip_address", "address")


@admin.register(ProductImage)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


@admin.register(ProductVideo)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "video")



