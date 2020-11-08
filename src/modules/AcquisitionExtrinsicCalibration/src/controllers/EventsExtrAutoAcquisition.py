from PySide2 import QtCore, QtWidgets, QtGui
import numpy as np
import cv2
import time
import os
from DataAcquisitionExtr import DataAcquisitionExtr

class EventsExtrAutoAcquisition():
    """
    Events for automatic extrinsic acquisition 
    """

    def __init__(self, window):
        super(EventsExtrAutoAcquisition).__init__()
        self.window = window
        self.camera = DataAcquisitionExtr()
        self.countNoImageAutoAcq = 0
        self.scalaImage = 90
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
        if (whichCamera == 'RGB-DEPTH'):
            self.whichCamera = 'RGB-DEPTH'
        if (whichCamera == 'RGB-THERMAL'):
            self.whichCamera = 'RGB-THERMAL'
            self.camera.initThermalCamera()
        self.createDirs()
        
    def turnOnCamera(self, whichCamera):
        self.chooseCamera(whichCamera)
        if (self.clicStart):
            self.viewCamera1.deleteLater()
            self.viewCamera2.deleteLater()
        self.initCamera()
        self.initCounter()
        return self.viewCamera1, self.viewCamera2

    def turnOffCamera(self):
        if (self.clicStart):
            self.viewCamera1.deleteLater()
            self.viewCamera2.deleteLater()
        self.timerCameras.stop()
        if self.whichCamera == 'RGB-THERMAL':
            self.camera.closeThermalCamera()
        self.countNoImageAutoAcq = 0
        self.clicStart = False

    def initCamera(self):
        self.timerCameras = QtCore.QTimer()
        self.timerCameras.setInterval(self.periodAcq*1000)
        self.timerCameras.timeout.connect(self.getFrameDrawPattern)
        self.timerCameras.start()
        self.widgetCamera1()
        self.widgetCamera2()
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

    def widgetCamera1(self):
        self.viewCamera1 = QtWidgets.QGraphicsView()
        scene1 = QtWidgets.QGraphicsScene()
        self.imagePixmap1 = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem1 = scene1.addPixmap(self.imagePixmap1)
        self.viewCamera1.setScene(scene1)
        
    def widgetCamera2(self):
        self.viewCamera2 = QtWidgets.QGraphicsView()
        scene2 = QtWidgets.QGraphicsScene()
        self.imagePixmap2 = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem2 = scene2.addPixmap(self.imagePixmap2)
        self.viewCamera2.setScene(scene2)

    def getFrameDrawPattern(self):
        if self.countNoImageAutoAcq < self.NoImagesAutoAcq:
            if (self.whichCamera == 'RGB-DEPTH'):
                frameCamera1, frameCamera2 = self.detectPattern(
                    self.camera.getRgbImage(), self.camera.getDepthImage())
            if (self.whichCamera == 'RGB-THERMAL'):
                frameCamera1, frameCamera2 = self.detectPattern(
                    self.camera.getRgbImage(), self.camera.getThermalImage())
            self.pixMapCamera1(frameCamera1)
            self.pixMapCamera2(frameCamera2)
        else:
            self.timerCameras.stop()

    def pixMapCamera1(self, frameCamera1):
        frameCamera1 = self.imageResize(
            frameCamera1, self.scalaImage)
        imageCamera1 = QtGui.QImage(
            frameCamera1, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap1 = QtGui.QPixmap.fromImage(imageCamera1)
        self.imagePixmapItem1.setPixmap(self.imagePixmap1)

    def pixMapCamera2(self, frameCamera2):
        frameCamera2 = self.imageResize(
            frameCamera2, self.scalaImage)
        imageCamera2 = QtGui.QImage(
            frameCamera2, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmap2 = QtGui.QPixmap.fromImage(imageCamera2)
        self.imagePixmapItem2.setPixmap(self.imagePixmap2)

    def detectPattern(self, image1, image2):        
        grayImage1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        grayImage2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        self.patternDimension = (
            self.patternDimension[1], self.patternDimension[0])
        self.findCorners1, self.corners1 = cv2.findChessboardCorners(
            grayImage1, self.patternDimension, flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        self.findCorners2, self.corners2 = cv2.findChessboardCorners(
            grayImage2, self.patternDimension, flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        if self.findCorners1 and self.findCorners2:
            self.subPixCorners(grayImage1, grayImage2)
            self.saveImages(image1, image2)
            image1, image2 = self.drawPattern(image1, image2)
            self.countNoImageAutoAcq += 1
            #time.sleep(0.5)
        return image1, image2

    def subPixCorners(self, grayImage1, grayImage2):
        self.corners1 = cv2.cornerSubPix(
            grayImage1, self.corners1, (11, 11), (-1, -1), self.criteria)
        self.corners2 = cv2.cornerSubPix(
            grayImage2, self.corners2, (11, 11), (-1, -1), self.criteria)

    def drawPattern(self, image1, image2):
        image1 = cv2.drawChessboardCorners(
            image1, self.patternDimension, self.corners1, self.findCorners1)
        image2 = cv2.drawChessboardCorners(
            image2, self.patternDimension, self.corners2, self.findCorners2)
        return image1, image2

    def createDirs(self):
        os.mkdir(self.pathImages)
        self.pathRgbImages = os.path.join(self.pathImages, 'rgb')
        os.mkdir(self.pathRgbImages)

        if self.whichCamera == 'RGB-DEPTH':
            self.pathDepthImages = os.path.join(self.pathImages, 'depth')
            os.mkdir(self.pathDepthImages)

        if self.whichCamera == 'RGB-THERMAL':
            self.pathThermalImages = os.path.join(self.pathImages, 'thermal')
            os.mkdir(self.pathThermalImages)

    def saveImages(self, image1, image2):
        nameImage1 = "%s%s%i%s" % (
            self.pathRgbImages,'/image', self.countNoImageAutoAcq, '.png')
        cv2.imwrite(nameImage1, image1)

        if self.whichCamera == 'RGB-DEPTH':
            nameImage2 = "%s%s%i%s" % (
                self.pathDepthImages, '/image', self.countNoImageAutoAcq, '.png')
            cv2.imwrite(nameImage2, image2)
            
        if self.whichCamera == 'RGB-THERMAL':
            nameImage2 = "%s%s%i%s" % (
                self.pathThermalImages, '/image', self.countNoImageAutoAcq, '.png')
            cv2.imwrite(nameImage2, image2)

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
