
from PySide2 import QtGui, QtWidgets
from PySide2 import *
import json
import numpy as np
import cv2
from ExtrinsicCameraCalibration import ExtrinsicCameraCalibration

class EventsExtrinsicCalibration():
    def __init__(self, window):
        super(EventsExtrinsicCalibration).__init__()
        self.window = window
        self.scalaImage = 60
        self.extrinsicCalibrationData = {}

    def selectDirectoryImages(self):
        relativePath = 'modules/ExtrinsicCalibration/data'
        pathImages = QtWidgets.QFileDialog.getExistingDirectory(
            self.window, "Select Directory", relativePath)
        return pathImages

    def showImage(self, pathImage):
        widgetImage = self.imageToQtWidget(pathImage)
        self.window.imageLayout.addWidget(widgetImage)

    def startExtrinsicCalibration(self, pathImagesSrc, pathImageDst):
        self.extrinsicCalibration = ExtrinsicCameraCalibration(self.window)
        self.numberCornersPattern = (
            int(self.window.cornersX.text()), int(self.window.cornersY.text()))
        chosenCamera = self.window.comboBox.currentText()
        self.extrinsicCalibration.setConfig(
            self.numberCornersPattern, chosenCamera)
        self.extrinsicCalibration.startExtrinsicCalibration(
            pathImagesSrc, pathImageDst)
        self.getExtrinsicParameters()

    def getExtrinsicParameters(self):
        self.homographyMatrix = self.extrinsicCalibration.getHomographyMatrix()
        self.showHomography()
        self.clearWorkspace()

    def getPatternImages(self):
        patternImagesSrc, patternImagesDst = self.extrinsicCalibration.getDrawChessBoardImages()
        self.showImage(patternImagesSrc[0])
        self.showImage(patternImagesDst[0])
        return patternImagesSrc, patternImagesDst

    def showHomography(self):
        newHomographyMatrix = np.zeros((3, 3))
        for i in range(3) :
            for j in range(3) :
                newHomographyMatrix[i][j] = str(
                    np.around(self.homographyMatrix[i][j], 5))
        text = """
        {
            homography: [
                \t"""+str(self.homographyMatrix[0])+"""\n
                \t"""+str(self.homographyMatrix[1])+"""\n
                \t"""+str(self.homographyMatrix[2])+"""\n
            ]
        }
        """
        self.window.textBrowser.setText(text)
        self.window.textBrowser.setReadOnly(True)

        self.extrinsicCalibrationData['homographyMatrix'] = self.homographyMatrix.tolist()
        print(self.extrinsicCalibrationData['homographyMatrix'])


        
    def saveDialog(self):
        print(self.extrinsicCalibrationData)
        relativePath = 'modules/ExtrinsicCalibration/data'
        pathFile, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.json')
        with open(pathFile+'.json', 'w') as outFile:
            json.dump(self.extrinsicCalibrationData, outFile)

    def resetParameters(self):
        self.homographyMatrix = np.zeros((3,3))
        self.showHomography()
        self.window.textBrowser.setText('')

    def clearWorkspace(self):
        for index in reversed(range(self.window.imageLayout.count())):
            layoutItem = self.window.imageLayout.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.imageLayout.removeWidget(widgetToRemove)

    def imageToQtWidget(self, frame):
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        widgetImage = QtWidgets.QGraphicsView()
        widgetImage.setScene(imageScene)
        return widgetImage

    def imageResize(self, pathImage, scalePercent):
        if (isinstance(pathImage, str)):
            image = cv2.imread(pathImage, cv2.IMREAD_UNCHANGED)
        else:
            image = pathImage
        h,  w = image.shape[:2]
        scala = scalePercent / 100
        self.dimensionsCamera =  [int(i) for i in np.array([w, h])*scala]
        dim = (int(w*scala), int(h*scala))
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized
