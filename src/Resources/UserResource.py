from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.User import User

import hashlib

hashlib.sha256()
class UserRegister(Resource):

    def post(self):

        #estructura del json que debe venir en el post y los campos que son requeridos
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

        #cifradp de la contraseña del usuarios
        encryptedPassword = hashlib.sha224(data['password'].encode('utf-8')).hexdigest()
        newUser = User(None, data['name'], data['lastName'], encryptedPassword, data['email'], None, None)

        #instancia de la clase de la entidad user para hacer consultas a la base de datos
        userDAO = UserDAO()
        userVerification = userDAO.findUserByEmail(newUser.email)
        #validar al usuario
        if userVerification:
            return {'message': 'User already exists with that email', 'data': {
                'name': userVerification.name,
                'lastName': userVerification.lastName,
                'email': userVerification.email
            }}, 400

        #validacion de que el usuario se creo correctamente
        if userDAO.create(newUser):
            return {'message': 'User created', 'data': {
                'name': newUser.name,
                'lastName': newUser.lastName,
                'email': newUser.email
            }}, 201

        return {'message': 'User not created', 'data': {
                'name': data.name,
                'lastName': data.lastName,
                'email': data.email
            }}, 400


from DataAccessLayer.DataAccessObject.IDAO.UserDAO import UserDAO
