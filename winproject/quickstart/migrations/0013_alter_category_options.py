# Generated by Django 4.2.1 on 2023-05-26 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0012_alter_category_options_alter_alcoholvolume_namerus_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-nameeng',), 'verbose_name': 'Категория напитка', 'verbose_name_plural': 'Категории напитков'},
        ),
    ]
