from rest_framework import serializers

from products.models import Product


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'supplier',
            'title',
            'product_model',
            'date_of_launch',
        )
