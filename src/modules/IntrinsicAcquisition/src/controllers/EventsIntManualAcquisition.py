from PySide2 import QtWidgets, QtCore, QtGui
import numpy as np
import cv2
from DataIntAcquisition import DataIntAcquisition


class EventsIntManualAcquisition():
    """ 
    Events for manual intrinsic acquisition 
    """
    
    def __init__(self):
        super(EventsIntManualAcquisition).__init__()
        self.camera = DataIntAcquisition()
        self.viewCamera = QtWidgets.QGraphicsView()
        self.scalaImage = 100
        self.clicPlay = False
        self.clicCapture = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)

    def chooseCamera(self, whichCamera):
        if (whichCamera == 'RGB'):
            self.whichCamera = 'RGB'
        if (whichCamera == 'DEPTH'):
            self.whichCamera = 'DEPTH'
        if (whichCamera == 'THERMAL'):
            self.camera.initThermalCamera()
            self.whichCamera = 'THERMAL'

    def turnOnCamera(self, whichCamera):
        self.chooseCamera(whichCamera)
        if (self.clicPlay or self.clicCapture):
            self.viewCamera.deleteLater()
        self.initCamera()
        return self.viewCamera

    def captureImage(self, whichCamera):
        frameImage = []
        if (self.clicPlay or self.clicCapture):
            self.viewCamera.deleteLater()
            self.timerCamera.stop()
        self.clicCapture = False
        self.clicPlay = False
        if (whichCamera == 'RGB'):
            frameImage = self.camera.captureRgbImage()
        if (whichCamera == 'DEPTH'):
            frameImage = self.camera.captureDepthImage()
        if (whichCamera == 'THERMAL'):
            frameImage = self.camera.captureThermalImage()
        self.imageToQtWidget(frameImage)
        self.clicCapture = True
        return self.viewCamera

    def saveImage(self, whichCamera, nameImage):
        if whichCamera == 'RGB':
            self.camera.saveRgbImage(nameImage)
        if whichCamera == 'DEPTH':
            self.camera.saveDepthImage(nameImage)
        if whichCamera == 'THERMAL':
            self.camera.saveThermalImage(nameImage)

    def turnOffCamera(self):
        if (self.clicPlay or self.clicCapture):
            self.viewCamera.deleteLater()
            self.timerCamera.stop()
        if self.whichCamera == 'THERMAL':
            self.camera.closeThermalCamera()
        self.clicCapture = False
        self.clicPlay = False

    def initCamera(self):
        self.timerCamera = QtCore.QTimer()
        self.timerCamera.setInterval(30)
        self.timerCamera.timeout.connect(self.getFrame)            
        self.timerCamera.start()
        self.viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        self.imagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem = scene.addPixmap(self.imagePixmap)
        self.viewCamera.setScene(scene)
        self.clicPlay = True

    def getFrame(self):
        frame = []
        if (self.whichCamera == 'RGB'):
            frame = self.camera.getRgbImage()
        if (self.whichCamera == 'DEPTH'):
            frame = self.camera.getDepthImage()
        if (self.whichCamera == 'THERMAL'):
            frame = self.camera.getThermalImage()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            frame = abs(255 - frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            #frame = self.camera.getThermalImage()
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera,QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap = QtGui.QPixmap.fromImage(image)
        self.imagePixmapItem.setPixmap(self.imagePixmap)


    def imageToQtWidget(self, frame):
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        self.viewCamera = QtWidgets.QGraphicsView()
        self.viewCamera.setScene(imageScene)

    def imageResize(self, pathImage, scalePercent):
        if (isinstance(pathImage, str)):
            image = cv2.imread(pathImage, cv2.IMREAD_UNCHANGED)
        else:
            image = pathImage
        width = int(image.shape[1] * scalePercent / 100)
        height = int(image.shape[0] * scalePercent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized
