from Util.BodyParser import BodyParser
from flask_restful import Resource
from flask_jwt import jwt_required
from Util.BodyParser import BodyParser
from flask import request

from DataAccessLayer.Tmdb import Tmdb


class Movie(Resource):

    def get(self):
        tmdb = Tmdb()
        args = request.args
        results = tmdb.filterMovies(args['page'], args['id'], args['gender'], args['name'])
        if results is None:
            return {'data': None, 'message': 'There is a error with the data base...'}, 500
        return {'response': results}
