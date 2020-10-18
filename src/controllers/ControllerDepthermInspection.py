from PySide2 import QtWidgets
from views.DepthermInspectionWidget import DepthermInspectionWidget
from views.managementUser.UserManagement import UserManagementWidget
from controllers.ControllerUserManagement import ControllerUserManagement

class ControllerDepthermInspection():
    """
    Main controller app Deptherm Inspection
    """
    def __init__(self):
        super(ControllerDepthermInspection).__init__()
        app = QtWidgets.QApplication([])
        self.depthermIspectionApp = DepthermInspectionWidget()
        self.window = self.depthermIspectionApp.window
        self.depthermIspectionApp.show()
        self.connectButtons()
        app.exec_()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonUserManage.clicked.connect(
            self.showUserManagement)

    def showUserManagement(self):
        """
        Handler button user management
        """
        self.cleanWorkspace()
        userManagementWidget = UserManagementWidget()
        self.window.layoutWorkspace.addWidget(userManagementWidget)
        ControllerUserManagement(userManagementWidget)

    def cleanWorkspace(self):
        """
        Clean worksspace remove all widget
        """
        for index in reversed(range(self.window.layoutWorkspace.count())):
            layoutItem = self.window.layoutWorkspace.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutWorkspace.removeWidget(widgetToRemove)
