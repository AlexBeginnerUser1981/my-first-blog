# Generated by Django 4.2.1 on 2023-05-25 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0010_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('-namerus',), 'verbose_name': 'Гастрономия', 'verbose_name_plural': 'Гастрономия'},
        ),
        migrations.RenameField(
            model_name='alcoholvolume',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='body',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='color',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='potion',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='productionmethod',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='rawmaterial',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='sugarvolume',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='namerus',
        ),
        migrations.RenameField(
            model_name='variety',
            old_name='name',
            new_name='namerus',
        ),
    ]
