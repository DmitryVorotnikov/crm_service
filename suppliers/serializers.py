from rest_framework import serializers

from products.models import Product
from suppliers.models import Supplier


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'product_model',
            'date_of_launch',
        )


class SupplierCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'who_is_the_supplier',
            'name',
            'email',
            'country',
            'city',
            'street',
            'building',
        )


class SupplierListRetrieveSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = (
            'id',
            'who_is_the_supplier',
            'level',

            'name',
            'email',
            'country',
            'city',
            'street',
            'building',
            'debt_to_supplier',

            'products',

            'created_at',
        )
