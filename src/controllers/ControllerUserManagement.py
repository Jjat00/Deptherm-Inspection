from PySide2 import QtWidgets
from views.managementUser.UserRegister import UserRegisterWidget
from views.managementUser.UserConsult import UserConsultWidget
from views.managementUser.UserUpdate import UserUpdateWidget
from views.managementUser.UserDelete import UserDeleteWidget
from controllers.ControllerRegisterUser import ControllerRegisterUser

class ControllerUserManagement():
    """
    Controller for user management form
    """

    def __init__(self, managemetWidget):
        super(ControllerUserManagement).__init__()
        self.window = managemetWidget.window
        self.connectButtons()
        managemetWidget.exec()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonRegisterUser.clicked.connect(
            self.showRegisterUserForm)
        self.window.buttonConsultUser.clicked.connect(
            self.showConsultUserForm)
        self.window.buttonUpdateUser.clicked.connect(
            self.showUpdateUserForm)
        self.window.buttonDeleteUser.clicked.connect(
            self.showDeleteUserForm)

    def showRegisterUserForm(self):
        """
        Handler button register user
        """
        userRegisterWidget = UserRegisterWidget()
        ControllerRegisterUser(userRegisterWidget)
        

    def showUpdateUserForm(self):
        """
        Handler button update user
        """
        updateUserWidget = UserUpdateWidget()
        updateUserWidget.exec()

    def showConsultUserForm(self):
        """
        Handler button consult user
        """
        consultUser = UserConsultWidget()
        consultUser.exec()

    def showDeleteUserForm(self):
        """
        Handler button delete user
        """
        userDelete = UserDeleteWidget()
        userDelete.exec()
