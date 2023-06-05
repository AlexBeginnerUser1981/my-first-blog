# Generated by Django 4.2.1 on 2023-05-25 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('name', models.CharField(db_column='name_rus', db_index=True, max_length=255, unique=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, db_column='description_rus', default=None, null=True, verbose_name='Описание')),
                ('nameeng', models.CharField(db_column='name_eng', db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('descriptioneng', models.TextField(blank=True, db_column='description_eng', default=None, null=True, verbose_name='Description')),
                ('namefra', models.CharField(db_column='name_fr', db_index=True, max_length=255, null=True, verbose_name='Nom')),
                ('descriptionfra', models.TextField(blank=True, db_column='description_fr', default=None, null=True, verbose_name='Description')),
                ('subcategory', models.ForeignKey(blank=True, db_column='subcategory', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.subcategory', verbose_name='Sub Category')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
    ]