# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-13 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.TextField()),
            ],
            options={
                'db_table': 'genre_info',
            },
        ),
        migrations.CreateModel(
            name='MoviesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.TextField()),
                ('imdb_score', models.FloatField()),
                ('name', models.TextField()),
                ('release_on', models.DateTimeField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'movies_info',
            },
        ),
        migrations.AddField(
            model_name='genreinfo',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.MoviesInfo'),
        ),
    ]
