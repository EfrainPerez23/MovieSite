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
        if self.id and self.name and self.password and self.email:
            return True
        return False

    @classmethod
    def CreateUser(cls, name, lastName, password, email):
        conn= pymysql.connect(host='localhost', port=3306, user='root', passwd='asd123', db='mydb')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO user (name, lastName, password, email) VALUES (%s, %s, %s, %s)",(name,lastName,password,email))
        return conn.commit()
    
    @classmethod
    def register_responde(cls, name, lastName, password, email):
        conn= pymysql.connect(host='localhost', port=3306, user='root', passwd='asd123', db='mydb')
        cursor=conn.cursor()
        json= {
            'name': name,
            'lastName': lastName,
            'password': password,
            'email': email
        }
        return json
    
    
    


    