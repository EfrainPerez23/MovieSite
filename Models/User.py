from DataAccessLayer.DataAccessObject.Dependencies.DTO import DTO
import pymysql



class User(DTO):
    
    def __init__(self, id, name, lastName, password, email, movieGender, movie):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.password = password
        self.email = email
        self.movieGender = movieGender
        self.movie = movie

    def isValid(self):
        if self.name and self.password and self.email:
            return True
        return False