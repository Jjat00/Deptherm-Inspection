from PySide2 import QtWidgets
from models.interfaces.UserDB import UserDB


class ControllerDeleteUser():
    """
    Controller for delete user form
    """

    def __init__(self, userDeleteWidget):
        super().__init__()
        self.window = userDeleteWidget.window
        self.connectButtons()
        userDeleteWidget.exec()
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
        self.window.buttonDeleteUser.clicked.connect(self.deleteUser)

    def deleteUser(self):
        """
        Handler button delete user
        """
        try:
            self.getVulesLineEdit()
            if self.ID != None and self.delete:
                userDB = UserDB()
                count = userDB.deleteUserByID(self.ID)
                if count != 0:
                    self.showMesagge("User deleted successfully")
                    self.cleanLineEdit()
                else:
                    self.showMesagge("User does not exist")
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
