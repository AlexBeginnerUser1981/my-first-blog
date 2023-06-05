# Generated by Django 4.2.1 on 2023-05-31 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0020_potion_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='brand',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='color',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='country',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='food',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='productionmethod',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='region',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='type',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.AddField(
            model_name='variety',
            name='url',
            field=models.URLField(blank=True, db_column='url', null=True, verbose_name='url'),
        ),
        migrations.CreateModel(
            name='ReadingLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datex', models.DateTimeField(auto_now=True, db_column='datex', null=True)),
                ('date1', models.DateTimeField(auto_now_add=True, db_column='datea', null=True)),
                ('name_rus', models.CharField(db_column='name_rus', db_index=True, max_length=255, null=True, verbose_name='наименование')),
                ('description_rus', models.TextField(blank=True, db_column='description_rus', default=None, null=True, verbose_name='описание')),
                ('name_eng', models.CharField(db_column='name_eng', db_index=True, default='default', max_length=255, verbose_name='name')),
                ('description_eng', models.TextField(blank=True, db_column='description_eng', default=None, null=True, verbose_name='description')),
                ('name_fra', models.CharField(db_column='name_fr', db_index=True, max_length=255, null=True, verbose_name='nom')),
                ('description_fra', models.TextField(blank=True, db_column='description_fr', default=None, null=True, verbose_name='description')),
                ('country', models.ForeignKey(blank=True, db_column='country', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quickstart.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Терминология',
                'verbose_name_plural': 'Терминология',
                'ordering': ('name_eng',),
            },
        ),
        migrations.AddConstraint(
            model_name='readinglabel',
            constraint=models.UniqueConstraint(fields=('name_rus', 'name_eng'), name='label_unique_index'),
        ),
    ]
