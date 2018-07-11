import tmdbsimple as tmdb
import app as app

class Tmdb():

    def __init__(self):
        tmdb.API_KEY = app.app.config.get('TMDB_API_KEY')

    def getMovieByPage(self, page):
        movies = tmdb.Movies()
        response = movies.now_playing(page=page)
        return response

    def getGenres(self):
        genres = tmdb.Genres()
        response = genres.movie_list()
        return response