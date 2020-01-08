from model.Student import *
from pathlib import Path
import pickle

class StudentDAO:
    studentTable = {
        "thong": Student("ST2", "Dinh Dat Thong", True, "18-09-1997"),
        "son": Student("ST3", "Nguyen Ngoc Son", False, "04-05-1996")
    }

    location = "database/studentTable"

    def createTable(self):
        # if file existed
        if Path(self.location).is_file():
            return
        
        f = open(self.location, "wb")
        f.write(pickle.dumps(self.studentTable))
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
            student = table[id]
            return student

        return None


    

