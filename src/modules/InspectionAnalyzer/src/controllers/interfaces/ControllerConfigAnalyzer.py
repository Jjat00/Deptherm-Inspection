from PySide2 import QtGui, QtWidgets, QtCore
import json
import numpy as np 

class ControllerConfigAnalyzer():
    def __init__(self,  window):
        print('init ControllerConfigAnalyzer')
        self.window = window

    def loadPath(self):
        """
        docstring
        """
        relativePath = '../data'
        pathImages = QtWidgets.QFileDialog.getOpenFileName(
            self.window, 'open file', relativePath, selectedFilter='*.json')
        return pathImages[0]

    def openFile(self, pathFile):
        with open(pathFile) as jsonFile:
                data = json.load(jsonFile)
        return data

    def loadIntrinsicMatrix(self):
        """
        docstring
        """
        path = self.loadPath()
        data = self.openFile(path)
        intrinsicMatrix = data['intrinsicMatrix']
        self.window.textBrowserIntrinsic.setText(str(intrinsicMatrix))

    def loadHomographyRgbTodepth(self):
        """
        docstring
        """
        path = self.loadPath()
        data = self.openFile(path)
        intrinsicMatrix = data['homographyMatrix']
        self.window.textBrowserH1.setText(str(intrinsicMatrix))

    def loadHomographyThermalToRgb(self):
        """
        docstring
        """
        path = self.loadPath()
        data = self.openFile(path)
        intrinsicMatrix = data['homographyMatrix']
        self.window.textBrowserH2.setText(str(intrinsicMatrix))
