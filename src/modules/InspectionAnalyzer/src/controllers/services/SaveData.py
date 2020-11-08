from PySide2 import QtWidgets
import cv2
import numpy as np
import json
from vedo import *

relativePath = 'modules/InspectionAnalyzer/data/images'

class SaveData():
    """
    Save all data inspectino analyzer
    """

    def __init__(self, window):
        print('init SaveData')
        self.window = window

    def saveDialog(self):
        pathImages = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.png')
        self.pathImages = pathImages[0]

    def saveRgbImage(self, rgbImage):
        """
        docstring
        """
        if self.pathImages != '':
            cv2.imwrite("%sRgb.png" % self.pathImages, rgbImage)

    def saveDepthImage(self, depthImage):
        """
        docstring
        """
        if self.pathImages != '':
            cv2.imwrite("%sDepth.png" % self.pathImages, depthImage)

    def saveThermalImage(self, thermalImage):
        """
        docstring
        """
        if self.pathImages != '':
            cv2.imwrite("%sThermal.png" % self.pathImages, thermalImage)

    def saveRgbThermalImage(self, rgbThermal):
        """
        docstring
        """
        if self.pathImages != '':
            cv2.imwrite("%sRgbThermal.png" % self.pathImages, rgbThermal)

    def saveDepthData(self, depthData):
        """
        docstring
        """
        pass
        if self.pathImages != '':
            np.save("%sDepthData" % self.pathImages, depthData)

    def savePointCloud(self, pointCloud, pointCloudVedo):
        """
        docstring
        """
        if self.pathImages != '':
            with open("%sPointCloud.json" % self.pathImages, 'w') as outFile:
                json.dump(pointCloud, outFile)
            write(pointCloudVedo, "%sPointCloud.ply" % self.pathImages)
