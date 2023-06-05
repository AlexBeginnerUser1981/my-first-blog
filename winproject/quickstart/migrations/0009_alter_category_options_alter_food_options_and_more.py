# Generated by Django 4.2.1 on 2023-05-25 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_potion_food_alter_potion_alcohol_alter_potion_sugar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-name',), 'verbose_name': 'Категория напитка', 'verbose_name_plural': 'Категории напитков'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('-name',), 'verbose_name': 'Гастрономия', 'verbose_name_plural': 'Гастрономия'},
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='Category',
            new_name='category',
        ),
    ]