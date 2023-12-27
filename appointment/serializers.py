from rest_framework import serializers
from .models import Appointment
from product.serializers import ProductSerializer
from .api import _is_valid
from rest_framework.validators import ValidationError


class AppointmentSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False)
    email = serializers.EmailField(required=False)
    phone_num = serializers.IntegerField(required=True)

    @classmethod
    def validate_phone_num(cls, value):
        validity = _is_valid(value)
        if not validity:
            raise ValidationError("Please enter the valid number")
        print("phone number is valid", value, validity)
        return value

    class Meta:
        model = Appointment
        fields = ("id", "product", "email", "phone_num")

    @classmethod
    def make_appointment(cls, validated_data):
        Appointment.objects.make_appointment(validated_data)
