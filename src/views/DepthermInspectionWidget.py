
import sys
import os
from PySide2 import QtCore, QtUiTools, QtWidgets
from views.styles.StyleDepthermInspection import StyleDepthermInspection
from views.LoginWidget import LoginWidget

class DepthermInspectionWidget(QtWidgets.QDialog):
    """
    Main Widget for Deptherm Inspection 
    """
    def __init__(self, *args, **kwargs):
        super(DepthermInspectionWidget, self).__init__(*args, **kwargs)
        #self.loginWidget = LoginWidget()
        self.initUI()
        StyleDepthermInspection(self)
    
    def closeEvent(self, event):
        print('User has pressed DepthermInspectionWidget the close button')
        sys.exit(0)

    def initUI(self):
        """ 
        Initialize the parameters
        """
        self.loadForm()
        self.setWindowTitle("Deptherm Inspection")
        self.setGeometry(0, 0, 1366, 750)

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
