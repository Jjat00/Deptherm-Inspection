
from PySide2 import QtCore, QtWidgets, QtUiTools
import sys
import os

from StyleInspectionAnalyzer import StyleInspectionAnalyzer


class InspectionAnalyzerWidget(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(InspectionAnalyzerWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        StyleInspectionAnalyzer(self)


    def __del__(self):
        print('Destructor called, InspectionAnalyzerWidget deleted.')

    def initUI(self):
        self.setWindowTitle("Camera Fusion")
        self.setGeometry(100, 50, 1170, 623)


    def loadForm(self):
        relativePath = 'modules/InspectionAnalyzer/src/'
        formUI = os.path.join(
            sys.path[0], '%sviews/InspectionAnalyzer.ui' % relativePath)
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

