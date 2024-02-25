from django.db import models

from suppliers.models import Supplier

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')

    title = models.CharField(max_length=300, verbose_name='Название')
    product_model = models.TextField(max_length=1500, verbose_name='Модель')
    date_of_launch = models.DateTimeField(verbose_name='Дата выхода', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)
