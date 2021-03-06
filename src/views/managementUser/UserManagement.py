import sys
import os
from PySide2 import QtWidgets, QtCore, QtUiTools
from views.styles.StyleUserManagement import StyleUserManagement


class UserManagementWidget(QtWidgets.QDialog):
    """
    Widget ofr user management (create, update delete, read)
    """

    def __init__(self, *args, **kwargs):
        super(UserManagementWidget, self).__init__(*args, **kwargs)
        self.initGUI()
        StyleUserManagement(self)

    def initGUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("User Register")
        self.setGeometry(200, 100, 930, 560)


    def closeEvent(self, event):
        print('User UserManagementWidget has pressed the close button')
        sys.exit(0)

    def loadForm(self):
        """
        load form.ui create in Qt designer
        """
        formUI = os.path.join(
            sys.path[0], 'views/managementUser/userManagement.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
