# Generated by Django 3.2.16 on 2024-06-10 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_ad_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]
