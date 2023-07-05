from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from validate_docbr import CPF, CNPJ
from django.core.exceptions import ValidationError
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException, is_valid_number
from rest_framework import serializers
from .models import User, ShiftOptions
from cloudinary import uploader


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Choose between " + " and".join(message) + "."


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This field must be unique."
            )
        ]
    )

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ]
    )

    def validate_cpfCnpj(self, value):
        if value:
            cpf_validator = CPF()
            cnpj_validator = CNPJ()

            if not cpf_validator.validate(value) and not cnpj_validator.validate(value):
                raise ValidationError("Invalid CPF or CNPJ.")
        return value

    def validate_cellphone(self, value):
        try:
            parsed_number = phonenumbers.parse(value, "BR")
            if not is_valid_number(parsed_number):
                raise serializers.ValidationError("Invalid phone number.")
        except NumberParseException:
            raise serializers.ValidationError("Invalid phone number format.")

        return value

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "gender",
            "first_name",
            "last_name",
            "address",
            "number",
            "complement",
            "city",
            "state",
            "country",
            "postalCode",
            "cellphone",
            "cpfCnpj",
            "foreignerDocument",
            "image",
            "is_superuser",
            "is_allowed",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "gender": {
                "error_messages": {
                    "invalid_choice": choices_error_message(ShiftOptions),
                }
            },
        }

    def create(self, validated_data: dict) -> User:
        image_file = validated_data.pop("image", None)
        user = User.objects.create_user(**validated_data)

        if image_file:
            upload_result = uploader.upload(image_file)
            image_url = upload_result.get("secure_url", "")
            user.image = image_url
            user.save()

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        image_file = validated_data.pop("image", None)
        instance = super().update(instance, validated_data)

        if image_file:
            upload_result = uploader.upload(image_file)
            image_url = upload_result.get("secure_url", "")
            instance.image = image_url
            instance.save()

        return instance
