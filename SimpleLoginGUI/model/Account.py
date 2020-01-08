class Account:

    # constructor
    def __init__(self, username=None, password=None, role=None):
        self.username = username
        self.password = password
        self.role = role

    # getters
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def getRole(self):
        return self.role

    # setters
    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password
    
    def setRole(self, role):
        self.role = role