from PySide2 import QtWidgets

from views.DepthermInspectionWidget import DepthermInspectionWidget
from views.managementUser.UserManagement import UserManagementWidget
from views.LoginWidget import LoginWidget
from views.configurationInspection.InspectionConfigurationWidget import InspectionConfigurationWidget
from views.configurationInspection.ClientFormWidget import ClientFormWidget

from controllers.ControllerUserLogin import ControllerUserLogin
from controllers.ControllerUserManagement import ControllerUserManagement

class MainControllerDepthermInspection():
    """
    Main controller app Deptherm Inspection
    """
    def __init__(self):
        super(MainControllerDepthermInspection).__init__()
        app = QtWidgets.QApplication([])
        self.depthermIspectionApp = DepthermInspectionWidget()
        self.window = self.depthermIspectionApp.window
        self.depthermIspectionApp.show()
        self.connectButtons()
        self.STATELOGIN = False
        app.exec_()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonUserManage.clicked.connect(
            self.showUserManagementWidget)
        self.window.buttonLogin.clicked.connect(
            self.showUserLoginWidget)
        self.window.buttonLogout.clicked.connect(
            self.logout)
        self.window.buttonInspection.clicked.connect(
            self.showInspectionConfigurationWidget)
        self.window.buttonCalibInt.clicked.connect(
            self.showIntrinsicCalibrationWidget)
        self.window.buttonClean.clicked.connect(
            self.cleanWorkspace)

    def showUserManagementWidget(self):
        """
        Handler button user management
        """
        self.cleanWorkspace()
        if self.STATELOGIN:
            userManagementWidget = UserManagementWidget()
            self.window.layoutWorkspace.addWidget(userManagementWidget)
            ControllerUserManagement(userManagementWidget)
        else:
            self.showMessage("you need to be logged like admin for this!")


    def showUserLoginWidget(self):
        """
        Handler button login user
        """
        self.cleanWorkspace()
        loginWidget = LoginWidget()
        self.window.layoutWorkspace.addWidget(loginWidget)
        ControllerUserLogin(self, loginWidget)

    def showInspectionConfigurationWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        
        clientFormWidgetWidget = ClientFormWidget()
        self.window.layoutWorkspace.addWidget(clientFormWidgetWidget)
        clientFormWidgetWidget.exec()


    def showIntrinsicCalibrationWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        
        inspectionConfigurationWidget = InspectionConfigurationWidget()
        self.window.layoutWorkspace.addWidget(inspectionConfigurationWidget)
        inspectionConfigurationWidget.exec()

    def cleanWorkspace(self):
        """
        Clean worksspace remove all widget
        """
        self.window.labelMessage.setText("")
        for index in reversed(range(self.window.layoutWorkspace.count())):
            layoutItem = self.window.layoutWorkspace.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutWorkspace.removeWidget(widgetToRemove)

    def showMessage(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)

    def logout(self):
        """
        Logout session user
        """
        if self.STATELOGIN:
            self.STATELOGIN = False
            self.showMessage("User logout")
        else:
            self.showMessage("Not logged in")
