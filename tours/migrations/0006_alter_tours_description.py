# Generated by Django 4.1.5 on 2023-06-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_cities_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Описание'),
        ),
    ]
