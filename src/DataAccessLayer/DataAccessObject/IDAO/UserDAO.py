from DataAccessLayer.DataAccessObject.Dependencies.DAO import DAO

from Models.User import User

from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager

class UserDAO(DAO):
    
    def create(self, user):
        if user.isValid():
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'INSERT INTO user VALUES (%s, %s, %s, %s, %s)'
            response = cursor.execute(query, (None, user.name, user.lastName, user.password, user.email,))
            if response:
                conn.connection.commit()
                return user
        
        return None

    @staticmethod
    def delete(cls, user):
        pass

    def read(self, id):
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT id, name, lastName, password, email FROM user WHERE id = %s'
        cursor.execute(query, (id,))
        firstUser = cursor.fetchone()
        if firstUser:
            user = User(firstUser['id'], firstUser['name'], firstUser['lastName'], firstUser['password'], firstUser['email'], None, None)
            return user
        return firstUser

    @staticmethod
    def readALL(cls):
        pass

    @staticmethod
    def update(self, user):
        pass
    
    def findUserByEmail(self, email):
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT id, name, lastName, password, email FROM user WHERE email = %s' 
        cursor.execute(query, (email,))
        userByEmail = cursor.fetchone()
        if userByEmail:
            user = User(userByEmail['id'], userByEmail['name'], userByEmail['lastName'], userByEmail['password'], userByEmail['email'], None, None)
            return user
        return userByEmail
