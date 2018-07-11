from Util.BodyParser import BodyParser
from flask_restful import Resource
from flask_jwt import jwt_required

from DataAccessLayer.Tmdb import Tmdb


class Movie(Resource):

    def get(self, page):
        tmdb = Tmdb()
        results = tmdb.getMovieByPage(page)
        if results:
            # genres = tmdb.getGenres()
            # # for genre in genres['genres']:
            # #         print(genre['id'])
            # for result in results['results']:
            #     print(result)
            return {'data': results}
        return {'data': None, 'message': 'There is a error with the data base...'}, 500
