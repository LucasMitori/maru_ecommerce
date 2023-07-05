from rest_framework import serializers
from .models import Purchase, ProductsPurchases
from products.serializers import ProductSerializer


class ProductsPurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsPurchases
        fields = ["id", "product", "price", "quantity", "discount", "total"]


class PurchaseSerializer(serializers.ModelSerializer):
    products = ProductsPurchasesSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ["id", "user", "payment_id", "purchase_status", "qr_code", "products"]
