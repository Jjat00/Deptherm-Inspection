from PySide2 import QtCore, QtUiTools, QtWidgets
import sys
import os
from Style import Styles


class AcquisitionManagementWidget(QtWidgets.QDialog):
    """
    Widget for login user
    """

    def __init__(self, *args, **kwargs):
        super(AcquisitionManagementWidget, self).__init__(*args, **kwargs)
        self.initUI()
        Styles(self)

    def initUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("Images Acquisition")
        self.setGeometry(200, 50, 500, 350)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/dataAcquisitionManagement.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
