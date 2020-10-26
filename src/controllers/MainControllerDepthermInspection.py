from PySide2 import QtWidgets


from views.managementUser.UserManagement import UserManagementWidget
from views.LoginWidget import LoginWidget
from views.configurationInspection.InspectionConfigurationWidget import InspectionConfigurationWidget
from views.configurationInspection.ClientFormWidget import ClientFormWidget

from controllers.ControllerUserLogin import ControllerUserLogin
from controllers.ControllerUserManagement import ControllerUserManagement

from views.AcquisitionManagementWidget import AcquisitionManagementWidget
from controllers.ControllerAcquisition import ControllerAcquisition

from MainControllerIntrinsicCalibration import MainControllerIntrinsicCalibration
from IntrinsicCalibrationWidget import IntrinsicCalibrationWidget


class MainControllerDepthermInspection():
    """
    Main controller app Deptherm Inspection
    """

    def __init__(self, depthermIspectionWidget):
        super(MainControllerDepthermInspection).__init__()
        self.window = depthermIspectionWidget.window
        depthermIspectionWidget.show()
        self.connectButtons()
        self.STATELOGIN = False
        #depthermIspectionWidget.exec()
        #app.exec_()

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

        self.window.buttonAcquisition.clicked.connect(
            self.showAcquisitionWidget)

    def showUserManagementWidget(self):
        """
        Handler button user management
        """
        if self.STATELOGIN:
            self.cleanWorkspace()
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
        intrinsicCalibrationWidget = IntrinsicCalibrationWidget()
        self.window.layoutWorkspace.addWidget(intrinsicCalibrationWidget)
        MainControllerIntrinsicCalibration(intrinsicCalibrationWidget)
        
        #inspectionConfigurationWidget = InspectionConfigurationWidget()
        #self.window.layoutWorkspace.addWidget(inspectionConfigurationWidget)
        #inspectionConfigurationWidget.exec()

    def showAcquisitionWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        acquisitionManagementWidget = AcquisitionManagementWidget()
        self.window.layoutWorkspace.addWidget(acquisitionManagementWidget)
        ControllerAcquisition(self, acquisitionManagementWidget)

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
            self.cleanWorkspace()
            self.STATELOGIN = False
            self.showMessage("User logout")
        else:
            self.showMessage("Not logged in")
