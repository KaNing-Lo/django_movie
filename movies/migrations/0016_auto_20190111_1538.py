# Generated by Django 2.1.1 on 2019-01-11 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20190111_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['date_added'], 'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='person',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 11, 15, 38, 2, 582270)),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, limit_choices_to={'production_roles': 2}, related_name='directed_movies', to='movies.Person', verbose_name='director'),
        ),
    ]
