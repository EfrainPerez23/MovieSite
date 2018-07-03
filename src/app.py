from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# Resources

from Resources.UserResource import User


app = Flask(__name__)

app.secret_key = 'movieRecomender'
api = Api(app)


api.add_resource(User, '/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
