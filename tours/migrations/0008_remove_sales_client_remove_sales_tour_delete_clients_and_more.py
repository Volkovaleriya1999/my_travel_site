# Generated by Django 4.1.5 on 2023-07-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='client',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='tour',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
