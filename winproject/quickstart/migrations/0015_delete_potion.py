# Generated by Django 4.2.1 on 2023-05-26 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0014_remove_potion_food'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Potion',
        ),
    ]
