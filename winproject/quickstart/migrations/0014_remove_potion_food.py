# Generated by Django 4.2.1 on 2023-05-26 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0013_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potion',
            name='food',
        ),
    ]