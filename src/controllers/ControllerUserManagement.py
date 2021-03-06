from PySide2 import QtWidgets
from views.managementUser.UserRegister import UserRegisterWidget
from views.managementUser.UserUpdate import UserUpdateWidget
from controllers.ControllerRegisterUser import ControllerRegisterUser
from controllers.ControllerUpdateUser import ControllerUpdateUser

from models.interfaces.UserDB import UserDB

class ControllerUserManagement():
    """
    Controller for user management form
    """

    def __init__(self, managemetWidget):
        super().__init__()
        self.window = managemetWidget.window
        userDB = UserDB()
        self.showUsers(userDB.getAllUser())
        self.connectButtons()
        managemetWidget.exec()
            

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        try:
            self.window.buttonRegisterUser.clicked.connect(
                self.showRegisterUserForm)
            self.window.buttonConsultAll.clicked.connect(
                self.showAll)
            self.window.buttonConsultUser.clicked.connect(
                self.showConsultUserForm)
            self.window.buttonUpdateUser.clicked.connect(
                self.showUpdateUserForm)
            self.window.buttonDeleteUser.clicked.connect(
                self.showDeleteUserForm)
        except:
            pass
    
    def showAll(self):
        userDB = UserDB()
        self.showUsers(userDB.getAllUser())
        self.showMesagge("")

    def showUsers(self, users):
        self.tableWidget = self.window.tableWidgetUsers
        # set row count
        self.tableWidget.setRowCount(10)
        # set column count
        self.tableWidget.setColumnCount(8)
        horHeaders = ['ID', 'name', 'lastname', 'type', 'state', 'cellphone', 'email', 'password']
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(147)

        for i in range(8):
            for j in range(10):
                self.tableWidget.setItem(
                    i, j, QtWidgets.QTableWidgetItem(''))

        print('users: ')
        for i in range (len(users)):
            type = ''
            if users[i].getUserType() == 1:
                type = 'admin'
            else:
                type  = 'operator'
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(users[i].getUserID())))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(users[i].getName()))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(users[i].getLastname()))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(type))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(users[i].getState())))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(users[i].getCellphone())))
            self.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(users[i].getEmail()))
            self.tableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(users[i].getPassword()))


    def showRegisterUserForm(self):
        """
        Handler button register user
        """
        print('registeeeeeeeeeeeeer')
        userRegisterWidget = UserRegisterWidget()
        ControllerRegisterUser(userRegisterWidget)
        self.showAll()
        

    def showUpdateUserForm(self):
        """
        Handler button update user
        """
        updateUserWidget = UserUpdateWidget()
        ControllerUpdateUser(updateUserWidget)
        self.showAll()

    def showConsultUserForm(self):
        """
        Handler button delete user
        """
        users = []
        try:
            self.getVulesLineEdit()
            if self.ID != None and self.delete:
                userDB = UserDB()
                user = userDB.getUserByID(self.ID)
                if user != None:
                    users.append(user)
                    self.showUsers(users)
                    self.showMesagge("")
                else:
                    self.showMesagge("User does not exists")
        except AttributeError:
            print("Fail update user")

    def showDeleteUserForm(self):
        """
        Handler button delete user
        """
        try:
            self.getVulesLineEdit()
            if self.ID != None and self.delete:
                userDB = UserDB()
                count = userDB.deleteUserByID(self.ID)
                self.showAll()
                if count == 0:
                    self.showMesagge("User does not exist")
        except AttributeError:
            print("Fail update user")

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

    def showMesagge(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)