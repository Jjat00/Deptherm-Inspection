from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
from DataIntAcquisition import DataIntAcquisition

class EventsIntAutoAcquisition():
    """
    Events for automatic intrinsic acquisition 
    """

    def __init__(self, window):
        super(EventsIntAutoAcquisition).__init__()
        self.window = window
        self.camera = DataIntAcquisition()
        self.countNoImageAutoAcq = 0
        self.scalaImage = 100
        self.clicStart = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)
        self.criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def setConfigAutoAcq(self, NoImages, periodAcq, patternDimension, pathImages):
        self.patternDimension = patternDimension
        self.NoImagesAutoAcq = NoImages
        self.periodAcq = periodAcq
        self.pathImages = pathImages

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
        if (self.clicStart):
            self.viewCamera.deleteLater()
        self.initCamera()
        self.initCounter()
        return self.viewCamera

    def turnOffCamera(self):
        if (self.clicStart):
            self.viewCamera.deleteLater()
            self.timerCamera.stop()
        if self.whichCamera == 'THERMAL':
            self.camera.closeThermalCamera()
        self.countNoImageAutoAcq = 0
        self.clicStart = False

    def initCamera(self):
        self.timerCamera = QtCore.QTimer()
        self.timerCamera.setInterval(self.periodAcq*1000)
        self.timerCamera.timeout.connect(self.getFrameDrawPattern)
        self.timerCamera.start()
        self.viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        self.imagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem = scene.addPixmap(self.imagePixmap)
        self.viewCamera.setScene(scene)
        self.clicStart = True

    def initCounter(self):
        self.timerCounter = QtCore.QTimer()
        self.timerCounter.setInterval(30)
        self.timerCounter.timeout.connect(self.setValueProgressBar)
        self.timerCounter.start()

    def setValueProgressBar(self):
        value = (self.countNoImageAutoAcq/self.NoImagesAutoAcq)*100
        self.window.progressBarAcq.setValue(value)
        self.window.labelNoImage.setText(str(self.countNoImageAutoAcq))

    def getFrameDrawPattern(self):
        frame = []
        if self.countNoImageAutoAcq < self.NoImagesAutoAcq:
            if (self.whichCamera == 'RGB'):
                print("get rgb image")
                frame = self.detectPattern(self.camera.getRgbImage())
            if (self.whichCamera == 'DEPTH'):
                print("get depth image")
                frame = self.detectPattern(self.camera.getDepthImage())
            if (self.whichCamera == 'THERMAL'):
                print("get thermal image")
                frame = self.detectPattern(self.camera.getThermalImage())
            frame = self.imageResize(frame, self.scalaImage)
            image = QtGui.QImage(
                frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.imagePixmap = QtGui.QPixmap.fromImage(image)
            self.imagePixmapItem.setPixmap(self.imagePixmap)
        else:
            self.timerCamera.stop()

    def detectPattern(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        patternDimension = (self.patternDimension[1], self.patternDimension[0])
        findCorners, corners = cv2.findChessboardCorners(
            gray, patternDimension, flags = cv2.CALIB_CB_NORMALIZE_IMAGE)
        if findCorners:
            corners = cv2.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), self.criteria)
            nameImage = "%s%i%s" % (self.pathImages, self.countNoImageAutoAcq, '.png')
            cv2.imwrite(nameImage, image)
            image = cv2.drawChessboardCorners(
                image, patternDimension, corners, findCorners)
            self.countNoImageAutoAcq += 1
            cv2.waitKey(200)
        return image

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
