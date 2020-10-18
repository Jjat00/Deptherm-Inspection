from PySide2 import QtWidgets
from models.entities.User import User
from models.interfaces.UserDB import UserDB

class ControllerRegisterUser():
    """
    Controller for register user form
    """

    def __init__(self, userRegisterWidget):
        super().__init__()
        self.window = userRegisterWidget.window
        self.connectButtons()
        userRegisterWidget.exec()

    def getVulesLineText(self):
        """
        get values fron line text form
        """
        pass

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonRegister.clicked.connect(
            self.registerUser)

    def registerUser(self):
        """
        Handler button register user
        """
        print("push")
