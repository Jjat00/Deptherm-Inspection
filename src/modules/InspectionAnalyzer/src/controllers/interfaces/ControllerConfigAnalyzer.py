from PySide2 import QtGui, QtWidgets, QtCore
import json
import numpy as np 

class ControllerConfigAnalyzer():
    def __init__(self,  window):
        print('init ControllerConfigAnalyzer')
        self.window = window
        self.extrinsicCalibrationData = {}

    def loadPath(self):
        """
        docstring
        """
        relativePath = '../modules/ExtrinsicCalibration/data'
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
        homographyMatrix = data['homographyMatrix']
        self.window.textBrowserH1.setText(str(homographyMatrix))

    def loadHomographyThermalToRgb(self):
        """
        docstring
        """
        path = self.loadPath()
        data = self.openFile(path)
        homographyMatrix = data['homographyMatrix']
        self.window.textBrowserH2.setText(str(homographyMatrix))
        self.extrinsicCalibrationData['homographyMatrix'] = homographyMatrix

    def saveConfiguration(self):
        """
        """
        print(self.extrinsicCalibrationData)
        with open('modules/InspectionAnalyzer/src/controllers/services/HThermal2rgb' + '.json', 'w') as outFile:
            json.dump(self.extrinsicCalibrationData, outFile)

