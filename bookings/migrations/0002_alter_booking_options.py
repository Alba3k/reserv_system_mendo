# Generated by Django 4.1.2 on 2022-10-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'бронирование номеров', 'verbose_name_plural': 'бронирование номеров'},
        ),
    ]
