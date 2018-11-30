from django import forms
from polls.models import *


class NameForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter user Name")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = PersonName
        fields = ('name',)


class RegForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Enter username")
    pwd = forms.CharField(widget=forms.PasswordInput, help_text="Enter password")

    class Meta:
        model = Register
        fields = ('username', 'pwd')


class AddGame(forms.ModelForm):
    game_name = forms.CharField(max_length=50, help_text="Enter Name of the game")
    game_type = forms.CharField(max_length=50, help_text="Enter type of game")
    game_description = forms.CharField(max_length=200, help_text="Describe the game")
    game_rating = forms.DecimalField(max_digits=2, decimal_places=1, help_text="Rate the game")
    game_manufacturer = forms.CharField(max_length=50, help_text="Enter Manufacturer's name")
    game_year = forms.IntegerField(help_text="Year the game was released")

    class Meta:
        model = GameItem
        fields = ('game_name', 'game_type', 'game_description', 'game_rating', 'game_manufacturer', 'game_year')


class AddBook(forms.ModelForm):
    book_name = forms.CharField(max_length=50, help_text="Enter Name of the book")
    book_type = forms.CharField(max_length=50, help_text="Enter type of book")
    book_description = forms.CharField(max_length=200, help_text="Describe the book")
    book_rating = forms.DecimalField(max_digits=2, decimal_places=1, help_text="Rate the book")
    book_author = forms.CharField(max_length=50, help_text="Enter author's name")
    book_year = forms.IntegerField(help_text="Year the game was released")

    class Meta:
        model = BookItem
        fields = ('book_name', 'book_type', 'book_description', 'book_rating', 'book_author', 'book_year')


class AddMovie(forms.ModelForm):
    movie_name = forms.CharField(max_length=50, help_text="Enter Name of the movie")
    movie_type = forms.CharField(max_length=50, help_text="Enter type of movie")
    movie_description = forms.CharField(max_length=200, help_text="Describe the movie")
    movie_rating = forms.DecimalField(max_digits=2, decimal_places=1, help_text="Rate the movie")
    movie_director = forms.CharField(max_length=50, help_text="Enter director's name")
    movie_year = forms.IntegerField(help_text="Year the game was released")

    class Meta:
        model = MovieItem
        fields = ('movie_name', 'movie_type', 'movie_description', 'movie_rating', 'movie_director', 'movie_year')
