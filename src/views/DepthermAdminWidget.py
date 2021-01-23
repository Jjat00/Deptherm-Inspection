import sys
import os
from PySide2 import QtWidgets, QtCore, QtUiTools
from views.styles.StyleAdminWidget import StyleAdminWidget


class DepthermAdminWidget(QtWidgets.QDialog):
    """
    docstring
    """

    def __init__(self):
        super().__init__()
        self.initGUI()
        StyleAdminWidget(self)

    def initGUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("User Register")
        self.setGeometry(0, 0, 1366, 750)

    def closeEvent(self, event):
        print('User UserManagementWidget has pressed the close button')
        sys.exit(0)

    def loadForm(self):
        """
        load form.ui create in Qt designer
        """
        formUI = os.path.join(
            sys.path[0], 'views/depthermAdminWidget.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
