from Util.BodyParser import BodyParser
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required



class Test(Resource):
    
    @jwt_required()
    def get(self):
        return {'hi': 111}