# Generated by Django 4.1.5 on 2023-05-28 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_address_profile_phone_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
