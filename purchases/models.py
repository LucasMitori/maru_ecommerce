from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_purchases",
        blank=True,
        null=True,
    )
    payment_id = models.IntegerField(unique=True)
    purchase_status = models.CharField(max_length=10, blank=False, null=False)
    qr_code = models.CharField(max_length=255)
    products = models.ManyToManyField(
        "products.Product", through="ProductsPurchases", related_name="purchase_set"
    )


class ProductsPurchases(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    total = models.IntegerField()
