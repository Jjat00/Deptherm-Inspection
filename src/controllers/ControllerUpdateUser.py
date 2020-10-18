from PySide2 import QtWidgets
from models.entities.User import User
from models.interfaces.UserDB import UserDB


class ControllerUpdateUser():
    """
    Controller for update user form
    """

    def __init__(self, userUpdateWidget):
        super().__init__()
        self.window = userUpdateWidget.window
        self.connectButtons()
        userUpdateWidget.exec()
        self.update = False

    def getVulesLineEdit(self):
        """
        get values fron line text form
        """
        try:
            self.showMesagge("")
            self.ID = int(self.window.lineEditID.text())
            self.name = self.window.lineEditName.text()
            self.lastname = self.window.lineEditLastname.text()
            self.email = self.window.lineEditEmail.text()
            self.phone = int(self.window.lineEditPhone.text())
            self.password = self.window.lineEditPassword.text()
            self.update = True
        except ValueError:
            self.showMesagge("incorrect data")
            self.update = False

    def getUserType(self):
        """
        Get user type from comoboBox
        """
        userType = self.window.comboBoxUserType.currentText()
        if userType == 'Admin':
            self.userType = 1
        if userType == 'Operator':
            self.userType = 2

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonUpdate.clicked.connect(self.updateUser)

    def updateUser(self):
        """
        Handler button register user
        """
        try:
            self.getVulesLineEdit()
            self.getUserType()
            if self.ID != None and self.update:
                userDB = UserDB()
                user = User(self.ID, self.userType, self.name, self.lastname,
                            True, self.phone, self.email, self.password)
                print(user.toString())
                count = userDB.updateUser(user)
                if count != 0:
                    self.showMesagge("Update user successfully")
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
        self.window.lineEditName.setText("")
        self.window.lineEditLastname.setText("")
        self.window.lineEditEmail.setText("")
        self.window.lineEditPhone.setText("")
        self.window.lineEditPassword.setText("")
        self.ID = None
