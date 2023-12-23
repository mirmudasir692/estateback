import tracemalloc

from django.db import models
tracemalloc.start()


class Discount(models.Model):
    event = models.CharField(max_length=100)
    start_on = models.DateTimeField(auto_now_add=True)
    end_on = models.DateTimeField(auto_now_add=False)
    percentage_discount = models.IntegerField()

    def __str__(self):
        return self.event


class CategoryManager(models.Manager):
    """
    this admin is for categories
    """
    def get_categories(self):
        categories = self.all()
        return categories


class Category(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="categories", null=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title

