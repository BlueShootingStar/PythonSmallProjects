from model.Teacher import *
from pathlib import Path
import pickle

class TeacherDAO:
    teacherTable = {
        "trung": Teacher("TC1", "Nguyen Quoc Hoang Trung", True, "30-04-1997", "Math"),
    }

    location = "database/teacherTable"

    def createTable(self):
        # if file existed
        if Path(self.location).is_file():
            return
        
        f = open(self.location, "wb")
        f.write(pickle.dumps(self.teacherTable))
        f.close()
    
    def readFromFile(self):
        f = open(self.location, "rb")
        table = pickle.loads(f.read())
        return table

    def selectAll(self):
        return self.readFromFile()

    def selectOne(self, id):
        table = self.readFromFile()

        if id in table:
            teacher = table[id]
            return teacher

        return None


    

