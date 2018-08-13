from Util.BodyParser import BodyParser
from flask_restful import Resource
from flask_jwt import jwt_required
from flask import request

from DataAccessLayer.Tmdb import Tmdb

from Models.Movie import Movie



class MovieResource(Resource):

    #endpoint de metodo GET que obtiene las peliculas segun el parametro que se le da
    #parametros: page, id, gender, name
    def get(self):
        tmdb = Tmdb()
        args = request.args
        results = tmdb.filterMovies(args['page'], args['id'], args['gender'], args['name'])
        if results is None:
            return {'data': None, 'message': 'There is a error with the data base...'}, 500
        return {'response': results}

    @jwt_required()
    def post(self):
        data = BodyParser.bodyParser([
            {
                'key': 'id',
                '_type': int,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'title',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'release_date',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'genre',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'poster_path',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },{
                'key': 'overview',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            }
            
        ])
        newMovie = Movie(data['id'], data['title'], data['genre'], data['overview'], data['poster_path'], ' ', data['release_date'])
        crated, movieDAO = MovieDAO().create(newMovie)

        if (crated):
            return {'data': {
                'name': data['title'],
                'id': data['id'],
                'genre': data['genre'],
                'overview': data['overview'],
                'imagePath': data['poster_path'],
                'videoPath': ' ',
                'date': data['release_date']
            }}, 201

        return {'data': movieDAO}, 409

    


class UserMovieResource(Resource):
    @jwt_required()
    def get(self):
        getFavoritesUserMovies = MovieDAO().getFavoritesUserMovies()
        if (getFavoritesUserMovies):
            return {'data': getFavoritesUserMovies}
        return {'data': []}

class MovieDeleteResource(Resource):
    @jwt_required()
    def delete(self, id):
        movieDAO = MovieDAO().delete(id)
        if (movieDAO):
            return {'data': movieDAO}, 200
        return {'data': movieDAO}, 400


from DataAccessLayer.DataAccessObject.IDAO.MovieDAO import MovieDAO


        
