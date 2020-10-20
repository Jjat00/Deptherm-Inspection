
import sys
import os
from PySide2 import QtCore, QtUiTools, QtWidgets
from views.styles.StyleDepthermInspection import StyleDepthermInspection
from views.LoginWidget import LoginWidget

class DepthermInspectionWidget(QtWidgets.QWidget):
    """
    Main Widget for Deptherm Inspection 
    """
    def __init__(self, *args, **kwargs):
        super(DepthermInspectionWidget, self).__init__(*args, **kwargs)
        #self.loginWidget = LoginWidget()
        self.initUI()
        StyleDepthermInspection(self)

    def initUI(self):
        """ 
        Initialize the parameters
        """
        self.loadForm()
        self.setWindowTitle("Deptherm Inspection")
        self.setGeometry(50, 50, 1080, 710)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/DethermInspection.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    depthermIspectionApp = DepthermInspectionWidget()
    depthermIspectionApp.show()
    app.exec_()
