# Generated by Django 2.1.1 on 2019-01-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20190109_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['full_name'], 'verbose_name_plural': 'people'},
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
