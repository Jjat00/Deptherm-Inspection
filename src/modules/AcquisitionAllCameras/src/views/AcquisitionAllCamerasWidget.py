from PySide2 import QtCore, QtUiTools, QtWidgets
from StylesAcquisitionWidgetAllCam import StylesAcquisitionWidgetAllCam
import cv2
import sys
import os

relativePath = 'modules/AcquisitionAllCameras/src/'


class AcquisitionAllCamerasWidget(QtWidgets.QDialog):
    """
    Main QTWidget for acquisition all cameras
    """
    def __init__(self, *args, **kwargs):
        super(AcquisitionAllCamerasWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        StylesAcquisitionWidgetAllCam(self)

    def initUI(self):
        self.setWindowTitle("Data Acquisition")
        self.setGeometry(100, 100, 1050, 585)

    def loadForm(self):
        formUI = os.path.join(
            sys.path[0], '%sviews/acquisitionAllCameras.ui' % relativePath)
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionAllCamerasWidget = AcquisitionAllCamerasWidget()
    acquisitionAllCamerasWidget.show()
    app.exec_()
