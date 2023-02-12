from django.db import models

from quarry.functions.overload_detection import overload_detection


class DumpTruckModels(models.Model):
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели самосвалов'

    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    load_capacity_max = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        verbose_name='Макс. грузоподъёмность',
    )

    def __str__(self):
        return self.name


class DumpTrucks(models.Model):
    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'

    tactical_number = models.CharField(
        max_length=12,
        verbose_name='Бортовой номер',
    )
    model = models.ForeignKey(
        DumpTruckModels,
        verbose_name='Модель',
        on_delete=models.CASCADE,
    )
    current_weight = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        verbose_name='Текущий вес',
        null=True,
        blank=True,
    )
    overload = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name='Перегруз, %',
        null=True,
        blank=True,
        editable=False
    )

    def __str__(self):
        return self.tactical_number

    def save(self, *args, **kwargs):
        print(self.overload)
        if self.current_weight:
            self.overload = overload_detection(
                self.model.load_capacity_max,
                self.current_weight
            )

        super(DumpTrucks, self).save(*args, **kwargs)
