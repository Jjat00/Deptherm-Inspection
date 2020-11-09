from PySide2 import QtGui, QtWidgets
import json
import numpy as np
import base64
import cv2
from IntrinsicCameraCalibration import IntrinsicCameraCalibration

class EventsIntrinsicCalibration():
    def __init__(self, window):
        super(EventsIntrinsicCalibration).__init__()
        self.window = window
        self.scalaImage = 100
        self.intrinsicCalibrationData = {}

    def selectDirectoryImages(self):
        relativePath = 'modules'
        pathImages = QtWidgets.QFileDialog.getExistingDirectory(
            self.window, "Select Directory", relativePath)
        return pathImages

    def showImage(self, pathImage):
        widgetImage = self.imageToQtWidget(pathImage)
        self.window.imageLayout.addWidget(widgetImage)

    def startIntrinsicCalibration(self, patternImages):
            self.intrinsicCalibration = IntrinsicCameraCalibration(self.window)
            self.numberCornersPattern = (
                int(self.window.cornersX.text()), int(self.window.cornersY.text()))
            self.intrinsicCalibration.setPatternDimensions(
                self.numberCornersPattern)
            self.intrinsicCalibration.startIntrinsicCalibration(patternImages)
            self.getIntrinsicParameters()

    def getIntrinsicParameters(self):
        self.intrinsicMatrix = self.intrinsicCalibration.getIntrinsicMatrix()
        self.showIntrinsicParamters()
        self.distortionParameters = self.intrinsicCalibration.getDistortionParameters()
        self.showDistortioParameters()
        self.clearWorkspace()

    def getPatternImage(self):
        patternImages = self.intrinsicCalibration.getDrawChessBoardImages()
        self.showImage(patternImages[0])
        #self.intrinsicCalibration.undistortImage1(patternImages[0])
        #self.intrinsicCalibration.undistortImage2(patternImages[0])
        return patternImages

    def showIntrinsicParamters(self):
        Fx = str(np.around(self.intrinsicMatrix[0][0], 6))
        Fy = str(np.around(self.intrinsicMatrix[1][1], 6))
        Cx = str(np.around(self.intrinsicMatrix[0][2], 6))
        Cy = str(np.around(self.intrinsicMatrix[1][2], 6))
        self.window.labelFx.setText(Fx)
        self.window.labelFy.setText(Fy)
        self.window.labelCx.setText(Cx)
        self.window.labelCy.setText(Cy)
        self.intrinsicCalibrationData['focalParameters'] = {
            'Fx': float(Fx),
            'Fy': float(Fy),
            'Cx': float(Cx),
            'Cy': float(Cy)
        }

    def showDistortioParameters(self):
        k1 = str(np.around(self.distortionParameters[0], 6))
        k2 = str(np.around(self.distortionParameters[1], 6))
        p1 = str(np.around(self.distortionParameters[2], 6))
        p2 = str(np.around(self.distortionParameters[3], 6))
        k3 = str(np.around(self.distortionParameters[4], 6))
        self.window.labelK1.setText(k1)
        self.window.labelK2.setText(k2)
        self.window.labelK3.setText(k3)
        self.window.labelP1.setText(p1)
        self.window.labelP2.setText(p2)
        self.intrinsicCalibrationData['distortionParameters'] = {
            'K1': float(k1),
            'K2': float(k2),
            'K3': float(k3),
            'p1': float(p1),
            'p2': float(p2)
        }

    def saveDialog(self):
        print(self.intrinsicCalibrationData)
        relativePath = 'modules/IntrinsicCalibration/data'
        pathFile, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.json')
        if pathFile != '':
            with open(pathFile+'.json', 'w') as outFile:
                json.dump(self.intrinsicCalibrationData, outFile)

    def getParameters(self):
        return self.intrinsicCalibrationData

    def getImagesCalibration(self):
        imagesCalibration = []
        images = self.intrinsicCalibration.getImagesCalibration()
        for img in images:
            imgBytes = cv2.imencode('.png', img)[1]
            pngStr = base64.b64encode(imgBytes)
            imagesCalibration.append(pngStr)
        return imagesCalibration

    def resetParameters(self):
        self.intrinsicMatrix = np.zeros((3,3))
        self.distortionParameters = np.zeros((1,5))[0]
        self.showIntrinsicParamters()
        self.showDistortioParameters()

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
