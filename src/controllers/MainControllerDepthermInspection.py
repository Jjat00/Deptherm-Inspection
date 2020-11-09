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

from ExtrinsicCalibrationWidget import ExtrinsicCalibrationWidget
from MainControllerExtCalibration import MainControllerExtCalibration

from MainControllerInspection import MainControllerInspection
from InspectionAnalyzerWidget import InspectionAnalyzerWidget

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
        self.inspectinoAnalyzer = False
        self.disabledButtuns()
        self.user = None
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

        self.window.buttonAcquisition.clicked.connect(
            self.showAcquisitionWidget)
            
        self.window.buttonCalibInt.clicked.connect(
            self.showIntrinsicCalibrationWidget)

        self.window.buttonCalibExt.clicked.connect(
            self.showExtrinsicCalibrationWidget)

        self.window.buttonClean.clicked.connect(
            self.cleanWorkspace)

        self.window.buttonInspectionAnalyzer.clicked.connect(
            self.showInspctionAnalyzer)

    def deleteObjet(self):
        """
        docstring
        """
        del self.userManagementWidget 
        del self.loginWidget 
        del self.clientFormWidgetWidget 
        del self.intrinsicCalibrationWidget 
        del self.extrinsicCalibrationWidget 
        del self.acquisitionManagementWidget 
        del self.analyzerWidget 

    def showUserManagementWidget(self):
        """
        Handler button user management
        """
        if self.STATELOGIN:
            self.cleanWorkspace()
            self.userManagementWidget = UserManagementWidget()
            self.window.layoutDepthermInpesction.addWidget(self.userManagementWidget)
            controller = ControllerUserManagement(self.userManagementWidget)
        else:
            self.showMessage("you need to be logged like admin for this!")


    def showUserLoginWidget(self):
        """
        Handler button login user
        """
        self.cleanWorkspace()
        self.loginWidget = LoginWidget()
        self.window.layoutDepthermInpesction.addWidget(self.loginWidget)
        controller = ControllerUserLogin(self, self.loginWidget)

    def showInspectionConfigurationWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.clientFormWidgetWidget = ClientFormWidget()
        self.window.layoutDepthermInpesction.addWidget(self.clientFormWidgetWidget)
        self.clientFormWidgetWidget.exec()


    def showIntrinsicCalibrationWidget(self):
        """
        docstring
        """
        print(self.user.toString())
        self.cleanWorkspace()
        self.intrinsicCalibrationWidget = IntrinsicCalibrationWidget()
        self.window.layoutDepthermInpesction.addWidget(self.intrinsicCalibrationWidget)
        controller = MainControllerIntrinsicCalibration(
            self, self.intrinsicCalibrationWidget)
        
        #inspectionConfigurationWidget = InspectionConfigurationWidget()
        #self.window.layoutDepthermInpesction.addWidget(inspectionConfigurationWidget)
        #inspectionConfigurationWidget.exec()

    def showExtrinsicCalibrationWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.extrinsicCalibrationWidget = ExtrinsicCalibrationWidget()
        self.window.layoutDepthermInpesction.addWidget(self.extrinsicCalibrationWidget)
        controller = MainControllerExtCalibration(self.extrinsicCalibrationWidget)

    def showAcquisitionWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.acquisitionManagementWidget = AcquisitionManagementWidget()
        self.window.layoutDepthermInpesction.addWidget(self.acquisitionManagementWidget)
        controller = ControllerAcquisition(self, self.acquisitionManagementWidget)

    def cleanWorkspace(self):
        """
        Clean worksspace remove all widget
        """
        self.window.labelMessage.setText("")

        if self.inspectinoAnalyzer:
            del self.analyzerWidget
            self.inspectinoAnalyzer = False

        for index in reversed(range(self.window.layoutDepthermInpesction.count())):
            layoutItem = self.window.layoutDepthermInpesction.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutDepthermInpesction.removeWidget(widgetToRemove)

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
            self.disabledButtuns()
        else:
            self.showMessage("Not logged in")

    def showInspctionAnalyzer(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.inspectinoAnalyzer = True
        self.analyzerWidget = InspectionAnalyzerWidget()
        self.window.layoutDepthermInpesction.addWidget(self.analyzerWidget)
        self.controllerMainInspection = MainControllerInspection(self.analyzerWidget)

    def disabledButtuns(self):
        self.window.buttonInspection.setEnabled(False)
        self.window.buttonAcquisition.setEnabled(False)
        self.window.buttonCalibInt.setEnabled(False)
        self.window.buttonCalibInt.setEnabled(False)
        self.window.buttonCalibExt.setEnabled(False)
        self.window.buttonInspectionAnalyzer.setEnabled(False)
        self.window.buttonReport.setEnabled(False)

    def enabledButtuns(self):
        self.window.buttonInspection.setEnabled(True)
        self.window.buttonAcquisition.setEnabled(True)
        self.window.buttonCalibInt.setEnabled(True)
        self.window.buttonCalibInt.setEnabled(True)
        self.window.buttonCalibExt.setEnabled(True)
        self.window.buttonInspectionAnalyzer.setEnabled(True)
        self.window.buttonReport.setEnabled(True)

