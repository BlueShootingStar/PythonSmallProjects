class Teacher:

    # constructor
    def __init__(self, id=None, name=None, gender=True, birthday=None, subject=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.subject = subject

    # getters
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getBirthday(self):
        return self.birthday
    
    def getSubject(self):
        return self.subject

    # setters
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setGender(self, gender):
        self.gender = gender

    def setBirthday(self, birthday):
        self.birthday = birthday

    def setSubject(self, subject):
        self.subject = subject
