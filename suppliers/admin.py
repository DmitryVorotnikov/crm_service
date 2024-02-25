from django.contrib import admin

from products.models import Product
from suppliers.models import Supplier


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0  # Количество дополнительных пустых форм для создания продуктов.


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
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
        'created_at',
    )

    inlines = [ProductInline]

    list_filter = ('country', 'city', 'who_is_the_supplier',)
    search_fields = ('country', 'name', 'email',)

    # Определяем действие для очистки поля debt_to_supplier.
    def clear_debt_to_supplier(self, request, queryset):
        # Обновляем выбранные объекты, устанавливая debt_to_supplier в None.
        queryset.update(debt_to_supplier=None)

    # Название действия в административной панели.
    clear_debt_to_supplier.short_description = "Очистить debt_to_supplier"

    # Регистрируем действие в административной панели.
    actions = ['clear_debt_to_supplier']
