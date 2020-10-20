from PySide2 import QtCore, QtUiTools, QtWidgets
import sys
import os
from views.styles.StyleLogin import StyleLogin

class LoginWidget(QtWidgets.QDialog):
    """
    Widget for login user
    """
    def __init__(self, *args, **kwargs):
        super(LoginWidget, self).__init__(*args, **kwargs)
        self.initUI()
        StyleLogin(self)

    def initUI(self):
        """
        Initialize parameters and components
        """
        self.loadForm()
        self.setWindowTitle("User Login")
        self.setGeometry(200, 50, 500, 350)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/login.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
