# Generated by Django 4.2.1 on 2023-05-25 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_potion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potion',
            name='appellation',
        ),
        migrations.AddField(
            model_name='potion',
            name='region',
            field=models.ForeignKey(blank=True, db_column='region', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.region', verbose_name='Region'),
        ),
    ]