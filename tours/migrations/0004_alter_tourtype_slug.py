# Generated by Django 4.1.5 on 2023-05-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_tourtype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourtype',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
    ]