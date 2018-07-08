from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# Resources
from Resources.UserResource import UserRegister,UserLogin

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')
api = Api(app)
api.add_resource(UserRegister, '/sign-up')
api.add_resource(UserLogin, '/login')




if __name__ == '__main__':
    app.run(debug=True)
