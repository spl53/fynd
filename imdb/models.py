from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class MoviesInfo(models.Model):
        popularity = models.FloatField()
	director = models.TextField()
	imdb_score = models.FloatField()
	name = models.TextField()
	release_on = models.DateTimeField()
	admin = models.ForeignKey(User)

        class Meta:
                """This is the table name in Database."""
                db_table = 'movies_info'


class GenreInfo(models.Model):
	movie = models.ForeignKey(MoviesInfo,related_name='genres')
	genre = models.TextField()

        class Meta:
                """This is the table name in Database."""
                db_table = 'genre_info'

	def __unicode__(self):
                return '%s' % (self.genres.genre)
