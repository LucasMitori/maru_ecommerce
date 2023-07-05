from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class ShiftOptions(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Default"


class User(AbstractUser):
    purchases = models.ForeignKey(
        "purchases.Purchase",
        on_delete=models.CASCADE,
        related_name="purchases",
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=50,
        choices=ShiftOptions.choices,
        default=ShiftOptions.DEFAULT,
        blank=True,
    )
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    number = models.CharField(max_length=10, blank=False, null=False)
    complement = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    postalCode = models.CharField(max_length=10, blank=False, null=False)
    cellphone = models.CharField(max_length=20, blank=False, null=False)
    cpfCnpj = models.CharField(max_length=14, blank=False, null=False)
    foreignerDocument = models.CharField(max_length=20, blank=False, null=False)
    image = CloudinaryField("user_images", blank=True)
    is_allowed = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Create your models here.
