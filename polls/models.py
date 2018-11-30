# Create your models here.

from django.db import models
from django import forms


class PersonName(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name


class Register(models.Model):
    username = models.CharField(max_length=128)
    pwd = models.CharField(max_length=128)


class GameItem(models.Model):
    gameid = models.IntegerField()
    game_name = models.CharField(max_length=50)
    game_type = models.CharField(max_length=50)
    game_description = models.CharField(max_length=200)
    game_rating = models.DecimalField(max_digits=2, decimal_places=1)
    game_manufacturer = models.CharField(max_length=50)
    game_year = models.IntegerField()


# Creates instances of this class in our databases
# specifies the field of our relations


class BookItem(models.Model):
    bookid = models.IntegerField()
    book_name = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    book_description = models.CharField(max_length=200)
    book_rating = models.DecimalField(max_digits=2, decimal_places=1)
    book_author = models.CharField(max_length=50)
    book_year = models.IntegerField()


# Creates instances of this class in our databases
# specifies the field of our relations


class MovieItem(models.Model):
    movieid = models.IntegerField()
    movie_name = models.CharField(max_length=50)
    movie_type = models.CharField(max_length=50)
    movie_description = models.CharField(max_length=200)
    movie_rating = models.DecimalField(max_digits=2, decimal_places=1)
    movie_director = models.CharField(max_length=50)
    movie_year = models.IntegerField()


# Creates instances of this class in our databases
# specifies the field of our relations
class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_path = models.CharField(max_length=200)
