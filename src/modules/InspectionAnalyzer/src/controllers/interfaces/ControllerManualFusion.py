from PySide2 import QtWidgets, QtGui
import numpy as np 
import glob
from PointCloud1 import PointCloud1
import cv2

class ManualFusion():
    def __init__(self, window):
        print('init ManualFusion')
        self.window = window
        self.pointCloud = PointCloud1()
        self.scalaImage = 30
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)

    def selectDirectoryImages(self):
        pathImages = QtWidgets.QFileDialog.getOpenFileName(
            self.window, "Select Directory", '../data', selectedFilter='*.png, *.npy')
        return pathImages

    def loadImage(self):
        pathImage = self.selectDirectoryImages()
        if pathImage != '':
            image = cv2.imread(pathImage[0])
            imageWidget = self.imageToQtWidget(image)
            self.window.layoutImages.addWidget(imageWidget)
        return image

    def loadRgbImage(self):
        self.rgbImage = self.loadImage()

    def loadDepthImage(self):
        pathImage = self.selectDirectoryImages()
        if pathImage != '':
            self.depthData = np.load(pathImage[0])
            depthImage = self.depthData.astype(np.uint8)
            depthImage = cv2.cvtColor(depthImage, cv2.COLOR_GRAY2BGR)
            imageWidget = self.imageToQtWidget(depthImage)
            self.window.layoutImages.addWidget(imageWidget)

    def loadThermalImage(self):
        self.ThermalImage = self.loadImage()

    def showPointCloud(self):
        print('[1]')
        self.pointCloud.setDepthData(self.depthData)
        widget, _ = self.pointCloud.showPointCloud()
        self.window.layoutPointCloudImages.addWidget(widget)

    def showColorPointCloud(self):
        print('[2]')
        self.pointCloud.setDepthData(self.depthData)
        self.pointCloud.setRgbImage(self.rgbImage)
        widget, _ = self.pointCloud.showColorPointCloud()
        self.window.layoutPointCloudImages.addWidget(widget)
    
    def showThermalPointCloud(self):
        print('[3]')
        self.pointCloud.setDepthData(self.depthData)
        self.pointCloud.setThermalImage(self.ThermalImage)
        widget = self.pointCloud.showThermalPointCloud()
        self.window.layoutPointCloudImages.addWidget(widget)

    def imageToQtWidget(self, frame):
        frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(frame, *self.dimensionsCamera,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        viewCamera = QtWidgets.QGraphicsView()
        viewCamera.setScene(imageScene)
        return viewCamera

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
