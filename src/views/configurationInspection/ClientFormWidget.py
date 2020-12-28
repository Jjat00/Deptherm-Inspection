from PySide2 import QtCore, QtUiTools, QtWidgets
import sys
import os
from views.styles.Style import Styles


class ClientFormWidget(QtWidgets.QDialog):
    """
    Widget for client form
    """

    def __init__(self, *args, **kwargs):
        super(ClientFormWidget, self).__init__(*args, **kwargs)
        self.initUI()
        Styles(self)

    def initUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("Inspection Configuration")
        self.setGeometry(450, 130, 478, 491)

    def loadForm(self):
        formUI = os.path.join(
            sys.path[0], 'views/configurationInspection/client.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
