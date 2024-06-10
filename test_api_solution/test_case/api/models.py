from django.db import models

from .constants import NAME_CONST_CHAR, MIN_CONST_FOR_VIEWS


class Ad(models.Model):
    """Модель описыващая добавленное обьявление."""

    title = models.CharField(
        'Заголовок',
        max_length=NAME_CONST_CHAR
    )
    author = models.CharField(
        verbose_name='Автор объявления',
        max_length=NAME_CONST_CHAR
    )
    views = models.PositiveIntegerField(
        'Количество просмотров',
        default=MIN_CONST_FOR_VIEWS
    )
    position = models.PositiveIntegerField(
        'Номер позиции'
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
