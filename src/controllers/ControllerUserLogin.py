from models.interfaces.UserDB import UserDB

from MainControllerDepthermInspection import MainControllerDepthermInspection
from DepthermInspectionWidget import DepthermInspectionWidget

from views.managementUser.UserManagement import UserManagementWidget
from controllers.ControllerUserManagement import ControllerUserManagement

class ControllerUserLogin():
    """
    Controller for login user form
    """

    def __init__(self, loginWidget):
        super().__init__()
        #self.mainWidget = mainWidget
        self.window = loginWidget.window
        self.connectButtons()
        self.loginWidget = loginWidget
        self.loginWidget.exec()
        self.consult = False
        

    def getVulesLineEdit(self):
        """
        get values fron line text form
        """
        try:
            self.showMesagge("")
            self.email = self.window.lineEditEmail.text()
            self.password = self.window.lineEditPassword.text()
            print(self.email)
            print(self.password)
            self.consult = True
        except ValueError:
            self.showMesagge("incorrect data")
            self.consult = False

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonLogin.clicked.connect(self.login)

    def login(self):
        """
        Handler button consult user
        """
        self.getVulesLineEdit()

        if self.email != None and self.consult:
            userDB = UserDB()
            user = userDB.getUserByEmail(self.email, self.password)
            if user != None:                    
                print(user.toString())
                self.showMesagge("Welcome %s" % user.getName())
                self.cleanLineEdit()
                self.loginWidget.hide()
                if user.userType == 2:
                    self.depthermIspectionWidget = DepthermInspectionWidget()
                    MainControllerDepthermInspection(user, self.depthermIspectionWidget)
                if user.userType == 1:
                    self.userManagementWidget = UserManagementWidget()
                    ControllerUserManagement(self.userManagementWidget)
            else:
                self.showMesagge("User does not exists")



    def showMesagge(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)

    def cleanLineEdit(self):
        """
        Clear line edit
        """
        #self.window.lineEditEmail.setText("")
        #self.window.lineEditPassword.setText("")
        self.email = None
