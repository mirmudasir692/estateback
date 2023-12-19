from django.contrib import admin
from .models import Discount, Category

"""
show the categories to the admin panel and 
discount model

"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "start_on", "end_on", "percentage_discount")
