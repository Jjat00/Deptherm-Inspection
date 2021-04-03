from PySide2 import QtCore, QtWidgets, QtGui
import numpy as np
import cv2
import time
import os
from DataAcquisitionAllCam import DataAcquisitionAllCam

class EventsAcquisitionAllCam():
    """
    Events for automatic extrinsic acquisition 
    """

    def __init__(self, window):
        super(EventsAcquisitionAllCam).__init__()
        self.window = window
        self.camera = DataAcquisitionAllCam()
        self.countNoImageAutoAcq = 0
        self.scalaImage = 60
        self.clicStart = False
        self.save = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)

    def setConfigAutoAcq(self, NoImages, period,  pathImages):
        self.NoImagesAutoAcq = NoImages
        self.period = period
        self.pathImages = pathImages
        self.createDirs()

    def startSaveImages(self):
        """
        init save images
        """
        self.save = True
        self.initCounter()
        self.timerCameras.setInterval(self.period*1000)

    def turnOnCameras(self):
        self.camera.initThermalCamera()
        if (self.clicStart):
            self.viewRgbCamera.deleteLater()
            self.viewDepthCamera.deleteLater()
            self.viewThermalCamera.deleteLater()
        self.initCamera()
        return self.viewRgbCamera, self.viewDepthCamera, self.viewThermalCamera

    def turnOffCamera(self):
        if (self.clicStart):
            self.viewRgbCamera.deleteLater()
            self.viewDepthCamera.deleteLater()
            self.viewThermalCamera.deleteLater()
        self.timerCameras.stop()
        self.camera.closeThermalCamera()
        self.countNoImageAutoAcq = 0
        self.save = False
        self.clicStart = False

    def initCamera(self):
        self.timerCameras = QtCore.QTimer()
        self.timerCameras.setInterval(30)
        self.timerCameras.timeout.connect(self.getFrameCameras)
        self.timerCameras.start()
        self.widgetRgbCamera()
        self.widgetDepthCamera()
        self.widgetThermalCamera()
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

    def widgetRgbCamera(self):
        self.viewRgbCamera = QtWidgets.QGraphicsView()
        rgbScene = QtWidgets.QGraphicsScene()
        self.rgbImagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.rgbImagePixmapItem = rgbScene.addPixmap(self.rgbImagePixmap)
        self.viewRgbCamera.setScene(rgbScene)
        
    def widgetDepthCamera(self):
        self.viewDepthCamera = QtWidgets.QGraphicsView()
        depthScene = QtWidgets.QGraphicsScene()
        self.depthImagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.depthImagePixmapItem = depthScene.addPixmap(self.depthImagePixmap)
        self.viewDepthCamera.setScene(depthScene)
        
    def widgetThermalCamera(self):
        self.viewThermalCamera = QtWidgets.QGraphicsView()
        thermalScene = QtWidgets.QGraphicsScene()
        self.thermalImagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.thermalImagePixmapItem = thermalScene.addPixmap(self.thermalImagePixmap)
        self.viewThermalCamera.setScene(thermalScene)

    def getFrameCameras(self):
        frameRgbCamera = self.camera.getRgbImage()
        frameDepthCamera = self.camera.getDepthImage()
        #frameThermalCamera = self.camera.getThermalImage()
        frame = self.camera.getThermalImage()
        #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        #frame = abs(255 - frame)
        #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frameThermalCamera = frame
        depthData = self.camera.getDepthData()
        self.pixMapRgbCamera(frameRgbCamera)
        self.pixMapDepthCamera(frameDepthCamera)
        self.pixMapThermalCamera(frameThermalCamera)
        self.saveImages(frameRgbCamera, frameDepthCamera,
                        frameThermalCamera, depthData)
        
    def pixMapRgbCamera(self, frameRgbCamera):
        frameRgbCamera = self.imageResize(
            frameRgbCamera, self.scalaImage)
        imageRgbCamera = QtGui.QImage(
            frameRgbCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.rgbImagePixmap = QtGui.QPixmap.fromImage(imageRgbCamera)
        self.rgbImagePixmapItem.setPixmap(self.rgbImagePixmap)

    def pixMapDepthCamera(self, frameDepthCamera):
        frameDepthCamera = self.imageResize(
            frameDepthCamera, self.scalaImage)
        imageDepthCamera = QtGui.QImage(
            frameDepthCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.depthImagePixmap = QtGui.QPixmap.fromImage(imageDepthCamera)
        self.depthImagePixmapItem.setPixmap(self.depthImagePixmap)

    def pixMapThermalCamera(self, frameThermalCamera):
        frameThermalCamera = self.imageResize(
            frameThermalCamera, self.scalaImage)
        imageThermalCamera = QtGui.QImage(
            frameThermalCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.thermalImagePixmap = QtGui.QPixmap.fromImage(imageThermalCamera)
        self.thermalImagePixmapItem.setPixmap(self.thermalImagePixmap)

    def createDirs(self):
        os.mkdir(self.pathImages)
        #directories for save rgb images
        self.pathRgbImages = os.path.join(self.pathImages, 'rgb')
        os.mkdir(self.pathRgbImages)
        #directories for save depth images
        self.pathDepthImages = os.path.join(self.pathImages, 'depth')
        os.mkdir(self.pathDepthImages)
        #directories for save thermal images
        self.pathThermalImages = os.path.join(self.pathImages, 'thermal')
        os.mkdir(self.pathThermalImages)

    def saveImages(self, rgbImage, depthImage, thermalImage, depthData):
        if self.save:
            if self.countNoImageAutoAcq < self.NoImagesAutoAcq:
                self.countNoImageAutoAcq += 1
                print("save images: ", self.countNoImageAutoAcq)
                #save rgb image in path rgb
                nameRgbImage = "%s%s%i%s" % (
                    self.pathRgbImages,'/image', self.countNoImageAutoAcq, '.png')
                cv2.imwrite(nameRgbImage, rgbImage)
                #save depth image in path depth
                nameDepthImage = "%s%s%i%s" % (
                    self.pathDepthImages, '/image', self.countNoImageAutoAcq, '.png')
                nameDepthData = "%s%s%i" % (
                    self.pathDepthImages, '/image', self.countNoImageAutoAcq)
                cv2.imwrite(nameDepthImage, depthImage)
                np.save(nameDepthData, depthData)
                #save thermal image in path thermal
                nameThermalImage = "%s%s%i%s" % (
                    self.pathThermalImages, '/image', self.countNoImageAutoAcq, '.png')
                cv2.imwrite(nameThermalImage, thermalImage)
            else:
                self.timerCameras.stop()
                self.timerCounter.stop()

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
