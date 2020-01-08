from model.Account import *
from model.Student import *
from model.Teacher import *
from helpers.ShareHelper import *
from view.frames.SignIn import *
from tkinter import *

class ProfileFrame:

    def __init__(self):

        # 1: create a frame(or window) object
        self.frame = Tk()
        self.frame.geometry("350x350")
        self.frame.title("TTS School")
        self.frame.resizable(False, False)
        # end of 1: create a frame(or window) object

        # 2: add child GUI components to frame
        Label(self.frame, text="Id: " + ShareHelper.currentUser.getId()).pack()
        Label(self.frame, text="Name: " + ShareHelper.currentUser.getName()).pack()
        if ShareHelper.currentUser.getGender() == True:
            Label(self.frame, text="Gender: Male").pack()
        else:
            Label(self.frame, text="Gender: Female").pack()
        Label(self.frame, text="Birthday: " + ShareHelper.currentUser.getBirthday()).pack()

        if ShareHelper.currentAccount.getRole() == "Teacher":
            Label(self.frame, text="Subject:" + ShareHelper.currentUser.getSubject()).pack()
        
        self.btnSignOut = Button(self.frame, text="Sign out", height=2, width=30, command=self.signOut).pack()
        # end of 2: add child GUI components to frame

        # 3: show GUI of frame object
        self.frame.mainloop()
        # end of 3: GUI of frame object

    def signOut(self, *args):
        self.frame.destroy()
        # SignInFrame()
    