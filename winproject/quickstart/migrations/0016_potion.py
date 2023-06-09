# Generated by Django 4.2.1 on 2023-05-26 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0015_delete_potion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('namerus', models.CharField(db_column='name_rus', db_index=True, max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, db_column='description_rus', default=None, null=True, verbose_name='Описание')),
                ('nameeng', models.CharField(db_column='name_eng', db_index=True, max_length=255, unique=True, verbose_name='Name')),
                ('descriptioneng', models.TextField(blank=True, db_column='description_eng', default=None, null=True, verbose_name='Description')),
                ('namefra', models.CharField(db_column='name_fr', db_index=True, max_length=255, null=True, verbose_name='Nom')),
                ('descriptionfra', models.TextField(blank=True, db_column='description_fr', default=None, null=True, verbose_name='Description')),
                ('alcohol', models.PositiveIntegerField(blank=True, db_column='alcoholvolume', null=True, verbose_name='Alcohol by volume')),
                ('sugar', models.PositiveIntegerField(blank=True, db_column='sugarvolume', null=True, verbose_name='Sugar by volume')),
                ('bod', models.ForeignKey(blank=True, db_column='winebod', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.body', verbose_name='Wine bod')),
                ('color', models.ForeignKey(blank=True, db_column='color', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.color', verbose_name='Color')),
                ('food', models.ManyToManyField(blank=True, db_column='food', related_name='potion_food', to='quickstart.food', verbose_name='Food')),
                ('manufacturer', models.ForeignKey(blank=True, db_column='manufacturer', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.manufacturer', verbose_name='Manufacturer')),
                ('productionmethod', models.ForeignKey(blank=True, db_column='productionmethod', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.productionmethod', verbose_name='Production Method')),
                ('region', models.ForeignKey(blank=True, db_column='region', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.region', verbose_name='Region')),
                ('type', models.ForeignKey(blank=True, db_column='type', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wine_type', to='quickstart.type', verbose_name='Type')),
                ('variety', models.ForeignKey(blank=True, db_column='variety', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.variety', verbose_name='Variety of Raw Material')),
            ],
            options={
                'verbose_name': 'Напиток',
                'verbose_name_plural': 'Напитки',
            },
        ),
    ]
