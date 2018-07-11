import tmdbsimple as tmdb
import app as app

class Tmdb(object):

    def __init__(self):
        tmdb.API_KEY = app.app.config.get('TMDB_API_KEY')

    def filterMovies(self, page, id, gender):
        if(page):
            response = tmdb.Movies()
            response = response.now_playing(page=page)
            return response
        if(id):
            movieInfo = tmdb.Movies(id).info()
            return movieInfo
        if(gender):
            genres = tmdb.Genres()
            response = genres.movie_list()
            return response
        
        return None