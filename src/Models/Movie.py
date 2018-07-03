from DataAccessLayer.DataAccessObject.Dependencies.DTO import DTO


class Movie(DTO):
    def __init__(self, id, name, gender, summary, imagePath, videoPath):
        self.id = id
        self.name = name
        self.gender = gender
        self.summary = summary
        self.imagePath = imagePath
        self.videoPath = videoPath

    def isValid(self):
        if self.id and self.name:
            return True
        return False
