from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplier',
        'title',
        'product_model',
        'date_of_launch',
    )
    list_filter = ('supplier',)
    search_fields = ('supplier', 'title', 'product_model',)
