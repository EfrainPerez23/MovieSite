from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# Resources

from Resources.UserResource import User


app = Flask(__name__)

app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')
api = Api(app)


api.add_resource(User, '/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
