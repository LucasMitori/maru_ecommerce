from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    tags = models.ManyToManyField("self", symmetrical=False, blank=True)
    reviews = models.ManyToManyField("Review", blank=True)
    product_available = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"


# Create your models here.
