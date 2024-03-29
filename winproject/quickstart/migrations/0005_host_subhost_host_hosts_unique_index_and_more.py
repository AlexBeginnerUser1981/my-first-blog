# Generated by Django 4.2.1 on 2023-11-13 13:11

from django.db import migrations, models
import django.db.models.deletion
import quickstart.models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_manufacturer_www_alter_wineglass_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('name_eng', models.CharField(blank=True, db_column='name_eng', db_index=True, help_text='name in english', max_length=255, null=True, verbose_name='name')),
                ('description_eng', models.TextField(blank=True, db_column='description_eng', default=None, help_text='description in english', null=True, verbose_name='description')),
                ('address', models.URLField(db_column='www', default=None, unique=True, verbose_name='host')),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Hosts',
                'ordering': ('name_eng',),
            },
        ),
        migrations.CreateModel(
            name='SubHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('name_eng', models.CharField(blank=True, db_column='name_eng', db_index=True, help_text='name in english', max_length=255, null=True, verbose_name='name')),
                ('description_eng', models.TextField(blank=True, db_column='description_eng', default=None, help_text='description in english', null=True, verbose_name='description')),
                ('address', models.CharField(blank=True, db_column='subhost', db_index=True, help_text='sudhost tail', max_length=255, null=True, verbose_name='subhost')),
                ('host', quickstart.models.ForeignKey(blank=True, db_column='host', help_text='site address', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subhosts', to='quickstart.host', verbose_name='host')),
            ],
            options={
                'verbose_name': 'SubHost',
                'verbose_name_plural': 'SubHosts',
                'ordering': ('name_eng',),
            },
        ),
        migrations.AddConstraint(
            model_name='host',
            constraint=models.UniqueConstraint(fields=('name_eng', 'address'), name='hosts_unique_index'),
        ),
        migrations.AddConstraint(
            model_name='subhost',
            constraint=models.UniqueConstraint(fields=('name_eng', 'address'), name='subhosts_unique_index'),
        ),
    ]
