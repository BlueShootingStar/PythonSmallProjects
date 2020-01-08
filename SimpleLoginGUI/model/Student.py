class Student:

    # constructor
    def __init__(self, id=None, name=None, gender=True, birthday=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday

    # getters
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getBirthday(self):
        return self.birthday

    # setters
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setGender(self, gender):
        self.gender = gender

    def setBirthday(self, birthday):
        self.birthday = birthday
