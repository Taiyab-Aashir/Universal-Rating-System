class GameImage:
    def __init__(self, mod, im):
        self.id=mod.id
        self.gameid = mod.gameid
        self.game_name = mod.game_name
        self.game_type = mod.game_type
        self.game_description = mod.game_description
        self.game_rating = mod.game_rating
        self.game_manufacturer = mod.game_manufacturer
        self.game_year = mod.game_year
        self.image = im

class BookImage:
    def __init__(self, mod, im):
        self.id=mod.id
        self.bookid = mod.bookid
        self.book_name = mod.book_name
        self.book_type = mod.book_type
        self.book_description = mod.book_description
        self.book_rating = mod.book_rating
        self.book_author = mod.book_author
        self.book_year = mod.book_year
        self.image = im

class MovieImage:
    def __init__(self, mod, im):
        self.id=mod.id
        self.movieid = mod.movieid
        self.movie_name = mod.movie_name
        self.movie_type = mod.movie_type
        self.movie_description = mod.movie_description
        self.movie_rating = mod.movie_rating
        self.movie_director = mod.movie_director
        self.movie_year = mod.movie_year
        self.image = im