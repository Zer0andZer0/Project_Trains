from django.db import models
from django.urls import reverse


class City(models.Model):  # Объявляю класс для создания моделей городов, максимум символов и уникальность
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):  # Объявляю функцию, для отображения названия города
        return self.name

    class Meta:  # Объявляю мету, для отображения вкладок
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']  # Сортировка городов
    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk})


