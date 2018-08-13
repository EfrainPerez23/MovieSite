import tmdbsimple as tmdb
import app as app

class Tmdb(object):

    #constructor que inicializa el api key
    def __init__(self):
        tmdb.API_KEY = app.app.config.get('TMDB_API_KEY')

    #filtrado de peliculas por pagina, id, genero y nombre
    def filterMovies(self, page, id, gender, name):
        response = None

        if(page and name == ''):
            response = tmdb.Movies()
            response = response.now_playing(page=page)
        if(id):
            response = tmdb.Movies(id).info()
        if(gender):
            genres = tmdb.Genres()
            response = genres.movie_list()
        if(name):
            response = tmdb.Search().movie(query=name, page=page)
        return response
