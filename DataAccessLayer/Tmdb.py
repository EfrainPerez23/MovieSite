import tmdbsimple as tmdb
import app as app

class Tmdb(object):

    #constructor que inicializa el api key
    def __init__(self):
        tmdb.API_KEY = app.app.config.get('TMDB_API_KEY')

    #filtrado de peliculas por pagina, id, genero y nombre
    def filterMovies(self, page, id, gender, name):
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
        if(name):
            response = tmdb.Search().movie(query=name)
            return response
        
        return None
