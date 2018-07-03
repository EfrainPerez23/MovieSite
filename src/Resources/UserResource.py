from Util.BodyParser import BodyParser
from flask_restful import Resource
from flask_jwt import jwt_required


class User(Resource):

    def get(self, name):
        return {'Hi': name}