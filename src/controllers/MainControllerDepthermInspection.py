from PySide2 import QtWidgets


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

    def __init__(self, user, depthermIspectionWidget):
        super(MainControllerDepthermInspection).__init__()
        self.window = depthermIspectionWidget.window
        #depthermIspectionWidget.show()
        self.connectButtons()
        self.STATELOGIN = False
        self.inspectinoAnalyzer = False
        #self.disabledButtuns()
        self.user = user
        self.window.labelHeader.setText("Deptherm operator: " + user.getName() + " " + user.getLastname())
        self.depthermIspectionWidget = depthermIspectionWidget
        self.depthermIspectionWidget.exec()
        #app.exec_()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """

        self.window.buttonLogout.clicked.connect(
            self.logout)

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

    def showExtrinsicCalibrationWidget(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.extrinsicCalibrationWidget = ExtrinsicCalibrationWidget()
        self.window.layoutDepthermInpesction.addWidget(self.extrinsicCalibrationWidget)
        controller = MainControllerExtCalibration(self, self.extrinsicCalibrationWidget)

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
        self.depthermIspectionWidget.hide()
        from views.LoginWidget import LoginWidget
        from controllers.ControllerUserLogin import ControllerUserLogin
        loginWidget = LoginWidget()
        ControllerUserLogin = ControllerUserLogin(loginWidget)

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

    def enabledButtuns(self):
        self.window.buttonInspection.setEnabled(True)
        self.window.buttonAcquisition.setEnabled(True)
        self.window.buttonCalibInt.setEnabled(True)
        self.window.buttonCalibInt.setEnabled(True)
        self.window.buttonCalibExt.setEnabled(True)
        self.window.buttonInspectionAnalyzer.setEnabled(True)

