"""
File: IntrinsicCalibrationWidget.py
Author: Jaimen Aza <<Jjat userjjar00@gmail.com>>
Date create: 19-august-2020
Last moditication date : 21-august-2020
"""

from StylesIntrinsicCalibration import StylesIntrinsicCalibration
from PySide2 import QtCore, QtUiTools, QtWidgets
import cv2
import sys
import os

relativePath = 'modules/IntrinsicCalibration/src/'

class IntrinsicCalibrationWidget(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(IntrinsicCalibrationWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        StylesIntrinsicCalibration(self)

    def initUI(self):
        self.setWindowTitle("Intrinsic Calibration")
        self.setGeometry(300, 100, 810, 560)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], '%sviews/intrinsicCalibration.ui' % relativePath)
        file = QtCore.QFile(formUI)        
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
