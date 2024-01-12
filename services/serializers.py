from rest_framework import serializers
from .models import Query
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import ValidationError
from product.serializers import ProductSerializer


class PhoneNumberSerializer(serializers.Serializer):
    number = PhoneNumberField(region="IN")


class QuerySerializer(serializers.ModelSerializer):
    phone_num = PhoneNumberField(required=True)
    email = serializers.EmailField(required=False)
    product = ProductSerializer(required=False)
    message = serializers.CharField(required=True)

    @classmethod
    def validate_phone_num(cls, value):
        phone_num = PhoneNumberSerializer(data={"number": value})
        if phone_num.is_valid():
            return value
        raise ValidationError("Please Enter Valid number")

    @classmethod
    def validate_message(cls, value):
        if not (value == "" or value is None):
            return value
        return ValidationError("Please Enter Proper Message")

    class Meta:
        model = Query
        fields = ("id", "message", "phone_num", "fulfilled", "email", "product")

    @classmethod
    def create(cls, validated_data):
        message = validated_data.get("message", None)
        phone_num = validated_data.get("phone_num", None)
        email = validated_data.get("email", None)
        product_id = validated_data.get("product_id", None)

        """ Get the data from the request and place query in the database"""

        Query.objects.add_query(product_id, message, email, phone_num)

