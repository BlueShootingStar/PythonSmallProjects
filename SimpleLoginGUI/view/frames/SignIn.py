from model.Account import *
from dao.AccountDAO import *
from dao.StudentDAO import *
from dao.TeacherDAO import *
from helpers.ShareHelper import *
from view.frames.Profile import *
from tkinter import *
from tkinter import messagebox

class SignInFrame:

    dao = AccountDAO()

    def __init__(self):
        # 1: create a frame(or window) object
        self.frame = Tk()
        self.frame.geometry("350x350")
        self.frame.title("TTS School")
        self.frame.resizable(False, False)
        self.frame.bind('<Return>', self.signIn) # press enter to call signIn function
        # end of 1: create a frame(or window) object

        # 2: add child GUI components to frame
        logo = PhotoImage(file="label-sign-in.png")
        Label(self.frame, image=logo).pack()

        Label(self.frame, text="Username").pack()
        self.txtUsername = Entry(self.frame, width=30)
        self.txtUsername.pack()

        Label(self.frame, text="Password").pack()
        self.txtPassword = Entry(self.frame, width=30, show='*')
        self.txtPassword.pack()

        self.btnSignIn = Button(self.frame, text="Sign in", height=2, width=30, command=self.signIn).pack()
        # end of 2: add child GUI components to frame

        # 3: show GUI of frame object
        self.frame.mainloop()
        # end of 3: GUI of frame object

    def signIn(self, *args):
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        account = Account(username, password)

        if self.isValidated() == False:
            messagebox.showwarning("Warning", "Please fill the text boxes!")
            return

        if self.isCorrectAccount(account) == False:
            messagebox.showerror("Error", "Account not found!")
            return

        if ShareHelper.currentAccount.getRole() == "Student":
            messagebox.showinfo("Information", "Student signed in")
        elif ShareHelper.currentAccount.getRole() == "Teacher":
            messagebox.showinfo("Information", "Teacher signed in")

        self.frame.destroy()
        ProfileFrame()
    
    # return true if account is correct , return False otherwise
    def isCorrectAccount(self, account):
        model = self.dao.selectOne(account.getUsername())

        if model == None:
            return False
        
        if model.getPassword() != account.getPassword():
            return False

        if model.getRole() == "Student":
            ShareHelper.currentUser = StudentDAO().selectOne(model.getUsername())
        elif model.getRole() == "Teacher":
            ShareHelper.currentUser = TeacherDAO().selectOne(model.getUsername())

        ShareHelper.currentAccount = model
        return True
    
    # return true if user filled the form, return False otherwise
    def isValidated(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()

        if username == "" or password == "":
            return False
        
        return True
