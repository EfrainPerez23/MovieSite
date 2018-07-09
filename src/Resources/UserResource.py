from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.User import User

import hashlib

hashlib.sha256()
class UserRegister(Resource):

    def post(self):

        data = BodyParser.bodyParser([
            {
                'key': 'name',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'lastName',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'password',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'email',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            }
        ])

        encryptedPassword = hashlib.sha224(data['password'].encode('utf-8')).hexdigest()
        newUser = User(None, data['name'], data['lastName'], encryptedPassword, data['email'], None, None)

        userDAO = UserDAO()
        userVerification = userDAO.findUserByEmail(newUser.email)
        if userVerification:
            return {'message': 'User already exists with that email', 'data': {
                'name': userVerification.name,
                'lastName': userVerification.lastName,
                'email': userVerification.email
            }}, 400

        if userDAO.create(newUser):
            return {'message': 'User created', 'data': data}, 201

        return {'message': 'User not created', 'data': data}, 400


from DataAccessLayer.DataAccessObject.IDAO.UserDAO import UserDAO
