from PySide2 import QtWidgets
from models.interfaces.UserDB import UserDB

class ControllerConsultUser():
    """
    Controller for consult user form
    """

    def __init__(self, userConsultWidget):
        super().__init__()
        self.window = userConsultWidget.window
        self.connectButtons()
        userConsultWidget.exec()
        self.delete = False

    def getVulesLineEdit(self):
        """
        get values fron line text form
        """
        try:
            self.showMesagge("")
            self.ID = int(self.window.lineEditID.text())
            self.delete = True
        except ValueError:
            self.showMesagge("incorrect data")
            self.delete = False

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonGetUser.clicked.connect(self.getUser)

    def getUser(self):
        """
        Handler button delete user
        """
        try:
            self.getVulesLineEdit()
            if self.ID != None and self.delete:
                userDB = UserDB()
                user = userDB.getUserByID(self.ID)           
                if user != None:
                    print(user.toString())
                    self.window.textBrowserGetUser.setText(user.toString())
                    self.cleanLineEdit()
                else:
                    self.showMesagge("User does not exists")
        except AttributeError:
            print("Fail update user")

    def showMesagge(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)

    def cleanLineEdit(self):
        """
        Clear line edit
        """
        self.window.lineEditID.setText("")
        self.ID = None
