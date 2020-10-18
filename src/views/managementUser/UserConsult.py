from PySide2 import QtWidgets, QtCore, QtUiTools
from views.styles.StyleUserManagement import StyleUserManagement
import sys
import os


class UserConsultWidget(QtWidgets.QDialog):
    """
    Widget to query the register
    """

    def __init__(self):
        super().__init__()
        self.initGUI()
        StyleUserManagement(self)

    def initGUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("User Consult")
        self.setGeometry(400, 100, 462, 460)

    def loadForm(self):
        """
        load form.ui create in Qt designer
        """
        formUI = os.path.join(
            sys.path[0], 'views/managementUser/userConsult.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
