# Generated by Django 4.2.1 on 2023-11-14 11:17

from django.db import migrations
import django.db.models.deletion
import quickstart.models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_parserlog_parserlog_parserlog_unique_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parserlog',
            name='subhost',
            field=quickstart.models.ForeignKey(blank=True, db_column='subhost', help_text='parser log', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parserlogs', to='quickstart.subhost', verbose_name='subhost'),
        ),
    ]
