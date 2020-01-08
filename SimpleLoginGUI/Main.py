from dao.AccountDAO import *
from dao.StudentDAO import *
from dao.TeacherDAO import *
from view.frames.SignIn import *
from helpers.ShareHelper import *

def createDatabase():
    AccountDAO().createTable()
    StudentDAO().createTable()
    TeacherDAO().createTable()

def main():
    createDatabase()
    SignInFrame()

main()
