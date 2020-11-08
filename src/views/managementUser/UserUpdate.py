from PySide2 import QtWidgets, QtCore, QtUiTools
from Style import Styles
import sys
import os


class UserUpdateWidget(QtWidgets.QDialog):
    """
    Widget to update users
    """

    def __init__(self):
        super().__init__()
        self.initGUI()
        Styles(self)

    def initGUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("Update User")
        self.setGeometry(400, 100, 450, 540)

    def loadForm(self):
        """
        load form.ui create in Qt designer to userUpdate
        """
        formUI = os.path.join(
            sys.path[0], 'views/managementUser/userUpdate.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
