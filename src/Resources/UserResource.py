from Util.BodyParser import BodyParser
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import request, jsonify
from Models.User import User
import datetime
import jwt
class UserRegister(Resource):
    
    def post(self):

        data=BodyParser.bodyParser([
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
        User.CreateUser(data['name'],data['lastName'],data['password'],data['email'])
        
        return User.register_responde(data['name'],data['lastName'],data['password'],data['email'])

class UserLogin(Resource):

    def post(self):
        data=BodyParser.bodyParser([
            {
                'key': 'email',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            },
            {
                'key': 'password',
                '_type': str,
                '_required': True,
                '_help': 'This field cannot be blank!'
            }
        ])
        token=jwt.encode({'email':data['password']},'donttell',algorithm='HS256')
        return jsonify({'token' : token.decode('UTF-8')})
            

            
    
        
        



