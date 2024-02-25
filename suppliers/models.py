from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Supplier(models.Model):
    who_is_the_supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)

    name = models.CharField(max_length=300, verbose_name='Название')
    email = models.EmailField(verbose_name='Email', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=400, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=400, verbose_name='Улица', **NULLABLE)
    building = models.CharField(max_length=400, verbose_name='Здание', **NULLABLE)
    debt_to_supplier = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        **NULLABLE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    level = models.SmallIntegerField(verbose_name='Уровень поставщика', **NULLABLE)

    def save(self, *args, **kwargs):
        # Если не передано значение в who_is_the_supplier или передано None.
        if self.who_is_the_supplier_id is None:
            self.level = 0
        else:
            # Получаем объект другого поставщика.
            other_supplier = Supplier.objects.get(id=self.who_is_the_supplier_id)
            # Устанавливаем уровень равный уровню другого поставщика плюс один.
            self.level = other_supplier.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('-created_at',)
