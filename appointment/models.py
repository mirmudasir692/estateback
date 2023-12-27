from django.db import models
from product.models import Product
from rest_framework.validators import ValidationError


class AppointmentManager(models.Manager):

    def make_appointment(self, validated_data):
        product_id = validated_data.get("product_id", None)
        phone_num = validated_data.get("phone_num", None)
        email = validated_data.get("email", None)
        product = Product.objects.get(id=product_id)
        if phone_num:
            return self.create(email=email, phone_num=phone_num, product=product)
        raise ValidationError("please enter the number")


class Appointment(models.Model):
    email = models.EmailField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False, blank=False)
    phone_num = models.PositiveBigIntegerField()

    objects = AppointmentManager()
