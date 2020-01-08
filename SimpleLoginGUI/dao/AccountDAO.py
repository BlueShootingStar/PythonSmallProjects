from model.Account import *
from pathlib import Path
import pickle

class AccountDAO:
    accountTable = {
        "trung": Account("trung", "123456", "Teacher"),
        "thong": Account("thong", "123", "Student"),
        "son": Account("son", "123456789", "Student"),
    }

    location = "database/accountTable"

    def createTable(self):
        # if file existed
        if Path(self.location).is_file():
            return
        
        f = open(self.location, "wb")
        f.write(pickle.dumps(self.accountTable))
        f.close()
    
    def readFromFile(self):
        f = open(self.location, "rb")
        table = pickle.loads(f.read())
        return table

    def selectAll(self):
        return self.readFromFile()

    def selectOne(self, username):
        table = self.readFromFile()

        if username in table:
            account = table[username]
            return account

        return None


    

