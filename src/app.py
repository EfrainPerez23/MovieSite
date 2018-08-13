from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, timedelta

# Resources
from Resources.UserResource import UserRegister
from Resources.test import Test
from Resources.MovieResource import MovieResource, UserMovieResource, MovieDeleteResource
app = Flask(__name__)

# Init of token security
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

# Load config File
app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')

# Init Rest API endpoints
api = Api(app)
api.add_resource(Test, '/test')
api.add_resource(UserRegister, '/sign-up')
api.add_resource(MovieResource, '/movies')
api.add_resource(MovieDeleteResource, '/movie/<int:id>')
api.add_resource(UserMovieResource, '/user_movie')

# Main function
if __name__ == '__main__':
    from Auth.Security import identity, authenticate
    jwt = JWT(app, authenticate, identity)

    @jwt.auth_response_handler
    def customized_response_handler(access_token, identity):
        return jsonify({
            'token': access_token.decode('utf-8'),
            'user': {
                'name': identity.name,
                'lastName': identity.lastName,
                'id': identity.id,
                'email': identity.email
            }
        })

    app.run()
