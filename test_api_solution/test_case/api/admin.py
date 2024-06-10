from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Настройка админ панели для объявлений."""

    empty_value_display = 'пусто'
    list_display = ('id', 'title', 'author', 'views', 'position',)
    search_fields = ('position',)
