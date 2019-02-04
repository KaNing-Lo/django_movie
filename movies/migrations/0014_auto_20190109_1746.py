# Generated by Django 2.1.1 on 2019-01-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_country_country_zh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='dislikes',
            new_name='favourites',
        ),
        migrations.AddField(
            model_name='movie',
            name='watches',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
