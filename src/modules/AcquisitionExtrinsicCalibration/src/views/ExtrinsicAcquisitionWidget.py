from PySide2 import QtCore, QtUiTools, QtWidgets
from Styles import Styles
import cv2
import sys
import os

relativePath = 'modules/AcquisitionExtrinsicCalibration/src/'


class ExtrinsicAcquisitionWidget(QtWidgets.QDialog):
    """
    Main QTWidget for extrinsic acquisition
    """
    def __init__(self, *args, **kwargs):
        super(ExtrinsicAcquisitionWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        Styles(self)

    def initUI(self):
        self.setWindowTitle("Data Acquisition")
        self.setGeometry(300, 100, 900, 540)

    def loadForm(self):
        formUI = os.path.join(
            sys.path[0], "%sviews/extrinsicAcquisition.ui" % relativePath)
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = ExtrinsicAcquisitionWidget()
    acquisitionExtrinsicCalibration.show()
    app.exec_()
