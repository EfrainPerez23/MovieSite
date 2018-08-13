from DataAccessLayer.DataAccessObject.Dependencies.DAO import DAO

from Models.Movie import Movie
import sys
from flask_jwt import current_identity


class MovieDAO(DAO):

    def create(self, movie):
        from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager
        if (movie.isValid()):
            conn = DBManager()
            cursor = conn.connection.cursor()
            if (self.findMovieById(movie) is None):
                query = 'INSERT INTO movie VALUES (%s, %s, %s, %s, %s, %s, %s)'
                createMovieRespone = cursor.execute(query, (movie.id, movie.name, movie.date, movie.gender, movie.imagePath, '', movie.summary,))
            if (self.findExistRelationUserMovie(movie) is False):
                query = 'INSERT INTO user_has_movie VALUES(%s, %s)'
                createMovieUser = cursor.execute(query, (current_identity.id, movie.id,))
                if createMovieUser:
                    conn.connection.commit()
                    return True, movie
            else:
                return False, 'There is already a relationship'
        return False, 'Object corrupted'

    
    def delete(self, _id):
        from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager
        if (_id):
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'DELETE FROM user_has_movie WHERE User_id = %s AND Movie_id = %s'
            response =  cursor.execute(query, (current_identity.id, _id))
            if (response):
                conn.connection.commit()
                return True
        return False



    
    def read(cls, id):
        pass


    
    def readALL(self):
        pass

    
    def update(self, movie):
        pass

    def findMovieById(self, movie):
        from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT id, name FROM movie WHERE id = %s' 
        cursor.execute(query, (movie.id,))
        movieById = cursor.fetchone()
        if movieById:
            return movie
        return movieById

    def getFavoritesUserMovies(self):
        from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'CALL getFavoritesUserMovies(%s);'
        cursor.execute(query, (current_identity.id,))
        response = cursor.fetchall()
        if (response):
            return response
        return None

    def findExistRelationUserMovie(self, movie):
        from DataAccessLayer.DataAccessObject.DataBase.DBManager import DBManager
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT User_id, Movie_id FROM user_has_movie WHERE User_id = %s AND Movie_id = %s'
        cursor.execute(query, (current_identity.id, movie.id,))
        response = cursor.fetchone()
        if (response):
            return True
        return False
