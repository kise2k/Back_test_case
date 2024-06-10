# Generated by Django 3.2.16 on 2024-06-09 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('position', models.PositiveIntegerField(verbose_name='Номер позиции')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления')),
            ],
            options={
                'verbose_name': 'Добавленное объявление',
                'verbose_name_plural': 'Добавленные объявления',
            },
        ),
    ]
