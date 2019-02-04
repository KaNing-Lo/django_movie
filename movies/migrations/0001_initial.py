# Generated by Django 2.1.1 on 2018-11-29 16:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'db_table': 'country',
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'genres',
                'db_table': 'genre',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('trailer', models.URLField()),
                ('cover', models.ImageField(upload_to='')),
                ('link_to_watch', models.URLField(blank=True, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('duration', models.DurationField(help_text='Format HH:MM:SS')),
                ('likes', models.IntegerField(blank=True, default=0)),
                ('dislikes', models.IntegerField(blank=True, default=0)),
                ('genres', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre', verbose_name='genres')),
                ('production_countries', models.ManyToManyField(related_name='movies', to='movies.Country', verbose_name='production countries')),
            ],
            options={
                'db_table': 'movie',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('date_of_death', models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people', to='movies.Country', verbose_name='represented country')),
            ],
            options={
                'verbose_name_plural': 'people',
                'db_table': 'person',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'production_role',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliked_movies', models.ManyToManyField(blank=True, related_name='users_disliked', to='movies.Movie', verbose_name='disliked movies')),
                ('favourite_movies', models.ManyToManyField(blank=True, related_name='users_favourite', to='movies.Movie', verbose_name='favourite movies')),
                ('liked_movies', models.ManyToManyField(blank=True, related_name='users_liked', to='movies.Movie', verbose_name='liked movies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('watch_list', models.ManyToManyField(blank=True, related_name='users_added_watch_list', to='movies.Movie', verbose_name='watch list')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='production_roles',
            field=models.ManyToManyField(blank=True, related_name='people', to='movies.ProductionRole', verbose_name='role in movie production'),
        ),
    ]
