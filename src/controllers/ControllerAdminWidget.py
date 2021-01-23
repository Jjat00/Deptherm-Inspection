from PySide2 import QtWidgets

from views.managementUser.UserManagement import UserManagementWidget
from controllers.ControllerUserManagement import ControllerUserManagement


class ControllerAdminWidget():
    """
    Controller for admin
    """ 

    def __init__(self, user, adminWidget):
        super().__init__()
        self.window = adminWidget.window
        self.connectButtons()
        self.user = user
        self.window.labelHeader.setText(
            "Deptherm Admin: " + user.getName() + " " + user.getLastname())
        self.adminWidget = adminWidget
        adminWidget.exec()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonManUser.clicked.connect(
            self.showUserManagemet)
        self.window.buttonReports.clicked.connect(
            self.showReports)
        self.window.buttonLogout.clicked.connect(
            self.logout)

    def showUserManagemet(self):
        """
        docstring
        """
        self.cleanWorkspace()
        self.userManagementWidget = UserManagementWidget()
        self.window.layoutUserManagement.addWidget(
            self.userManagementWidget)
        controllerUserManagement = ControllerUserManagement(self.userManagementWidget)
        
    def showReports(self):
        """
        docstring
        """
        self.cleanWorkspace()

    def logout(self):
        """
        Logout session user
        """
        self.adminWidget.hide()
        from views.LoginWidget import LoginWidget
        from controllers.ControllerUserLogin import ControllerUserLogin
        loginWidget = LoginWidget()
        ControllerUserLogin = ControllerUserLogin(loginWidget)

    def cleanWorkspace(self):
        """
        Clean worksspace remove all widget
        """
        for index in reversed(range(self.window.layoutUserManagement.count())):
            layoutItem = self.window.layoutUserManagement.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutUserManagement.removeWidget(widgetToRemove)
