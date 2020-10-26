from PySide2 import QtCore, QtUiTools, QtWidgets
from StylesIntAcqWidget import StylesIntAcqWidget
import cv2
import sys
import os

relativePath = 'modules/IntrinsicAcquisition/src/'

class IntrinsicAcquisitionWidget(QtWidgets.QDialog):
    """
    Main QTWidget for intrinsic acquisition
    """    

    def __init__(self, *args, **kwargs):
        super(IntrinsicAcquisitionWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        StylesIntAcqWidget(self)

    def initUI(self):
        self.setWindowTitle("Intrisic Acquisition")
        self.setGeometry(300, 100, 705, 600)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], relativePath + 'views/intrinsicAcquisition.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionIntrinsicCalibration = IntrinsicAcquisitionWidget()
    acquisitionIntrinsicCalibration.show()
    app.exec_()
