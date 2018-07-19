from DataAccessLayer.DataAccessObject.Dependencies.DTO import DTO


class MovieGender(DTO):

    def __init__(self, id, name, user):
        self.id = id
        self.name = name
        self.user = user

    def isValid(self):
        if self.id and self.name:
            return True
        return False
