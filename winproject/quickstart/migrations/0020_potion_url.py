# Generated by Django 4.2.1 on 2023-05-31 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0019_alter_body_name_eng_alter_brand_name_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='potion',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
    ]
