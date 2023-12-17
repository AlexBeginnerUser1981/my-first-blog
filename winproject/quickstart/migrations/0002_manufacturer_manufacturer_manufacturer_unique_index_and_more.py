# Generated by Django 4.2.1 on 2023-11-09 09:41

from django.db import migrations, models
import django.db.models.deletion
import quickstart.models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('name_rus', models.CharField(blank=True, db_column='name_rus', db_index=True, help_text='наименование на русском языке', max_length=255, null=True, verbose_name='наименование')),
                ('description_rus', models.TextField(blank=True, db_column='description_rus', default=None, help_text='описание на русском языке', null=True, verbose_name='описание')),
                ('name_eng', models.CharField(blank=True, db_column='name_eng', db_index=True, help_text='name in english', max_length=255, null=True, verbose_name='name')),
                ('description_eng', models.TextField(blank=True, db_column='description_eng', default=None, help_text='description in english', null=True, verbose_name='description')),
                ('name_fra', models.CharField(db_column='name_fr', db_index=True, help_text='наименование на французском языке', max_length=255, null=True, verbose_name='nom')),
                ('description_fra', models.TextField(blank=True, db_column='description_fr', default=None, help_text='описание на французском языке', null=True, verbose_name='la description')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
                'ordering': ('name_rus',),
            },
        ),
        migrations.AddConstraint(
            model_name='manufacturer',
            constraint=models.UniqueConstraint(fields=('name_rus', 'name_eng'), name='manufacturer_unique_index'),
        ),
        migrations.AddField(
            model_name='drink',
            name='manufacturer',
            field=quickstart.models.ForeignKey(blank=True, db_column='manufacturer', help_text='Производитель', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wines', to='quickstart.manufacturer', verbose_name='Производитель'),
        ),
    ]
