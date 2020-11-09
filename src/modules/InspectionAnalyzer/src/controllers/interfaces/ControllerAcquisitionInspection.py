import base64
from DataAcquisitionInpAnalyzer import DataAcquisitionInpAnalyzer
from PointCloud2 import PointCloud2
from Transformation import Transformation
from Analizer import Analyzer
from Registration import Registration
from SaveData import SaveData
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import json
import cv2
import os


class ControllerAcquisitionInspection():
    def __init__(self, window):
        print('init ControllerAcquisitionInspection')
        self.window = window

        self.acquisition = DataAcquisitionInpAnalyzer()

        self.transformation = Transformation()

        self.initParameters()

        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)

        self.initCheckBox()

    def initParameters(self):
        """
        docstring
        """
        self.counterAcqData = 0
        self.groupDepthData = []
        self.groupRgbImage = []
        self.groupPointCloud = []
        self.groupColorPointCloud = []
        self.LengthPointCloud = []
        self.colorImagePointCloud = []
        self.pointCloud = {}
        self.pointCloudVedo = None
        self.scalaImage = 30
        self.clicStart = False
        self.clicCapture = False
        self.maxThreshold = False
        self.minThreshold = False
        self.filterKn = False
        self.filterClean = True

    def initCheckBox(self):
        """
        docstring
        """
        self.window.checkBoxMax.stateChanged.connect(self.clickBoxMaxThreshold)
        self.window.checkBoxMin.stateChanged.connect(self.clickBoxMinThreshold)
        self.window.checkBoxClean.stateChanged.connect(self.clickBoxClean)
        self.window.checkBoxFilter.stateChanged.connect(self.clickBoxFilter)

    def turnOnCameras(self):
        if (self.clicStart or self.clicCapture):
            self.clearWorkspace()
        self.acquisition.initThermalCamera()

        self.setPseudoColor()
        self.window.comboBoxPseudColor.currentIndexChanged.connect(
            self.setPseudoColor)
        self.setColorRegister()
        self.window.comboBoxColorICP.currentIndexChanged.connect(
            self.setColorRegister)

        self.initCamera()
        return self.viewRgbCamera, self.viewDepthCamera, self.viewThermalCamera

    def turnOffCamera(self):
        if (self.clicStart or self.clicCapture):
            self.clearWorkspace()
        self.timerCameras.stop()
        self.clicStart = False
        self.clicCapture = False

    def initCamera(self):
        self.timerCameras = QtCore.QTimer()
        self.timerCameras.setInterval(30)
        self.timerCameras.timeout.connect(self.getFrameCameras)
        self.timerCameras.start()
        self.widgetRgbCamera()
        self.widgetDepthCamera()
        self.widgetThermalCamera()
        self.clicStart = True

    def widgetRgbCamera(self):
        self.viewRgbCamera = QtWidgets.QGraphicsView()
        rgbScene = QtWidgets.QGraphicsScene()
        self.imagePixmapRgb = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem1 = rgbScene.addPixmap(self.imagePixmapRgb)
        self.viewRgbCamera.setScene(rgbScene)

    #def pixMapRgbCamera(self, frameRgbCamera):
    #    frameRgbCamera = self.imageResize(frameRgbCamera, self.scalaImage)
    #    imageRgbCamera = QtGui.QImage(
    #        frameRgbCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
    #    self.imagePixmapRgb = QtGui.QPixmap.fromImage(imageRgbCamera)
    #    self.imagePixmapItem1.setPixmap(self.imagePixmapRgb)

    def widgetDepthCamera(self):
        self.viewDepthCamera = QtWidgets.QGraphicsView()
        depthScene = QtWidgets.QGraphicsScene()
        self.imageDepthPixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItemDepth = depthScene.addPixmap(self.imageDepthPixmap)
        self.viewDepthCamera.setScene(depthScene)

    def widgetThermalCamera(self):
        self.viewThermalCamera = QtWidgets.QGraphicsView()
        thermalScene = QtWidgets.QGraphicsScene()
        self.imagePixmapThermal = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItemThermal = thermalScene.addPixmap(self.imagePixmapThermal)
        self.viewThermalCamera.setScene(thermalScene)
    
    def getFrameCameras(self):
        self.frameRgbCamera = self.acquisition.getRgbImage()

        self.frameDepthCamera = self.acquisition.getDepthImage()

        #self.frameThermalCamera = self.acquisition.getThermalImage()
        frame = self.acquisition.getThermalImage()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = abs(255 - frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        self.frameThermalCamera = frame

        self.pixMapRgbCamera(self.frameRgbCamera)
        self.pixMapDepthCamera(self.frameDepthCamera)
        self.pixMapThermalCamera(self.frameThermalCamera)
        if self.clicCapture:
            #if self.counterPointCloud < 2:
            self.captureDepthData = self.acquisition.getDepthData()
            self.capturePointCloud()

    def captureImage(self, numberImages):
        period = float(self.window.lineEditFramesS.text())
        self.timerCameras.setInterval(period*1000)
        #QtWidgets.QMessageBox.about(
        #    self.window, "About aplicatoin", "This is simple")
        self.clicCapture = True
        self.counterPointCloud = 0

        self.numberPointsCloud = numberImages     

        self.captureRgbImage = self.frameRgbCamera
        self.captureDepthImage = self.frameDepthCamera
        self.captureThermal = self.frameThermalCamera

    def setColorRegister(self):
        """
        docstring
        """
        choosenColor = self.window.comboBoxColorICP.currentText()
        if choosenColor == 'colorless':
            self.colorRegister = 'colorless'
        if choosenColor == 'rgb':
            self.colorRegister = 'rgb'
        if choosenColor == 'thermal':
            self.colorRegister = 'thermal'
        if choosenColor == 'rgb-thermal':
            self.colorRegister = 'rgb-thermal'
        

    def setPseudoColor(self):
        """
        docstring
        """
        chosenCamera = self.window.comboBoxPseudColor.currentText()
        if chosenCamera == 'rainbow':
            self.nameFalseColor = 'rainbow'
        if chosenCamera == 'jet':
            self.nameFalseColor = 'jet'
        if chosenCamera == 'hsv':
            self.nameFalseColor = 'hsv'
        if chosenCamera == 'magma':
            self.nameFalseColor = 'magma'
        if chosenCamera == 'rainbow-inv':
            self.nameFalseColor = 'rainbow-inv'
        if chosenCamera == 'summer':
            self.nameFalseColor = 'summer'
        if chosenCamera == 'winter':
            self.nameFalseColor = 'winter'
        if chosenCamera == 'cool':
            self.nameFalseColor = 'cool'
        if chosenCamera == 'pink':
            self.nameFalseColor = 'pink'
        if chosenCamera == 'hot':
            self.nameFalseColor = 'hot'
        if chosenCamera == 'parula':
            self.nameFalseColor = 'parula'
        if chosenCamera == 'inferno':
            self.nameFalseColor = 'inferno'
        if chosenCamera == 'plasma':
            self.nameFalseColor = 'plasma'
        if chosenCamera == 'viridis':
            self.nameFalseColor = 'viridis'
        if chosenCamera == 'turbo':
            self.nameFalseColor = 'turbo'
        if chosenCamera == 'None':
            self.nameFalseColor = ''

    def getRgbImageWidget(self):
        """
        docstring
        """
        frame = self.captureRgbImage
        self.colorImagePointCloud = frame

        self.transformation.setRgbImage(frame)
        self.transformation.setColorImage(frame)

        scalaImage = 90
        frame = self.imageResize(frame, scalaImage)
        dimension = np.array([640, 480])*(scalaImage/100)
        rgbWidget = self.imageToQtWidget(frame, dimension)
        return rgbWidget

    def getDepthImageWidget(self):
        """
        docstring
        """
        print("get depth image widget")
        frame = self.captureDepthImage
        
        analyzerImage = Analyzer()
        analyzerImage.setImageToAnalyzer(frame)
        analyzerImage.setFalseColor(self.nameFalseColor)
        depthFalseColor = analyzerImage.getFalseColor()

        self.transformation.setDepthImage(depthFalseColor)
        newDepthImage = self.transformation.depthToRgbImage()

        self.transformation.setColorImage(newDepthImage)

        self.colorImagePointCloud = newDepthImage

        scalaImage = 90
        frame = self.imageResize(depthFalseColor, scalaImage)
        dimension = np.array([640, 480])*(scalaImage/100)
        depthWidget = self.imageToQtWidget(frame, dimension)
        return depthWidget

    def getThermalImageWidget(self):
        """
        docstring
        """
        frame = self.captureThermal
        analyzerImage = Analyzer()
        analyzerImage.setImageToAnalyzer(frame)
        analyzerImage.setFalseColor(self.nameFalseColor)
        
        maxUmbral = self.window.sliderMaxUmbral.value()
        minUmbral = self.window.sliderMinUmbral.value()
        if self.maxThreshold:
            analyzerImage.setMaxUmbral(maxUmbral)
        if self.minThreshold:
            analyzerImage.setMinUmbral(minUmbral)
        if self.maxThreshold and self.minThreshold:
            analyzerImage.setMinMaxUmbral(minUmbral, maxUmbral)

        newImage = analyzerImage.getFalseColor()

        self.transformation.setThermalImage(newImage)
        newThermalImage = self.transformation.thermalToRgbImage()
        self.transformation.setColorImage(newThermalImage)

        self.colorImagePointCloud = newThermalImage

        self.thermalImagePointCloud = newImage
        
        scalaImage = 90
        frame = self.imageResize(newImage, scalaImage)
        dimension = np.array([640, 480])*(scalaImage/100)
        thermalWidget = self.imageToQtWidget(frame, dimension)
        return thermalWidget

    def getDepthRgbImageWidget(self):
        """
        docstring
        """
        depthImage = self.captureDepthImage
        rgbImage = self.captureRgbImage

        analyzerImage = Analyzer()
        analyzerImage.setImageToAnalyzer(depthImage)
        analyzerImage.setFalseColor(self.nameFalseColor)
        depthImage = analyzerImage.getFalseColor()

        self.transformation.setRgbImage(rgbImage)
        newRgbImage = self.transformation.rgbToDepthImage()

        visibRgb = self.window.sliderVisibRgb.value()
        visibDepth = self.window.sliderVisibIR.value()
        image = cv2.addWeighted(depthImage, visibDepth / 100,
                                newRgbImage, visibRgb / 100, 0)

        self.transformation.setDepthImage(image)
        newRgbDepthImage = self.transformation.depthToRgbImage()
        self.transformation.setColorImage(newRgbDepthImage)

        scalaImage = 90
        frame = self.imageResize(image, scalaImage)
        dimension = np.array([640, 480])*(scalaImage/100)
        thermalWidget = self.imageToQtWidget(frame, dimension)
        return thermalWidget

    def getThermalRGBWidget(self):
        """
        docstring
        """
        frame = self.captureThermal
                
        self.transformation.setThermalImage(frame)
        newThermal = self.transformation.thermalToRgbImage()

        analyzerImage = Analyzer()
        analyzerImage.setImageToAnalyzer(newThermal)
        analyzerImage.setRgbImage(self.captureRgbImage)
        analyzerImage.setFalseColor(self.nameFalseColor)
        #analyzerImage.setMaxUmbral(0)

        maxUmbral = self.window.sliderMaxUmbral.value()
        minUmbral = self.window.sliderMinUmbral.value()
        if self.maxThreshold:
            print('set max umbral')
            analyzerImage.setMaxUmbral(maxUmbral)
        if self.minThreshold:
            print('set min umbral')
            analyzerImage.setMinUmbral(minUmbral)
        if self.maxThreshold and self.minThreshold:
            analyzerImage.setMinMaxUmbral(minUmbral, maxUmbral)

        visibRgb = self.window.sliderVisibRgb.value()
        visibThermal = self.window.sliderVisibIR.value()

        newImage = analyzerImage.getFusionImage(visibThermal, visibRgb)

        self.transformation.setColorImage(newImage)

        self.colorImagePointCloud = newImage
        scalaImage = 90
        frame = self.imageResize(newImage, scalaImage)
        dimension = np.array([640, 480])*(scalaImage/100)
        thermalRgbWidget = self.imageToQtWidget(frame, dimension)
        return thermalRgbWidget

    def capturePointCloud(self):
        """         
        Capture n poits cloud
        """
        print("capturing points: ", self.counterPointCloud)
        transformation = Transformation()

        transformation.setRgbImage(self.frameRgbCamera)
        transformation.setThermalImage(self.frameThermalCamera)
        transformation.setDepthData(self.captureDepthData)

        depthPoint = self.window.horizontalSliderDepth.value()
        xyzPoints = transformation.depth2xyz(depthPoint / 10)

        if self.colorRegister == 'rgb':
            colorImage = transformation.getColorRgb()
        if self.colorRegister == 'thermal':
            colorImage = transformation.getTemperature()
        if self.colorRegister == 'rgb-thermal':
            rgbImage = transformation.getTemperature()
            thermalImage = transformation.getTemperature()
        else:
            colorImage = transformation.getColorRgb()

        self.groupPointCloud.append(xyzPoints)
        self.groupColorPointCloud.append(colorImage)

        self.LengthPointCloud.append(len(xyzPoints))
        self.counterPointCloud = self.counterPointCloud+1
        self.window.labelCloudCaptured.setText(str(self.counterPointCloud))
        if self.counterPointCloud >= int(self.numberPointsCloud):
            self.timerCameras.stop()
            self.clicCapture = False
            self.acquisition.closeThermalCamera()

    def getGroupPointCloud(self):
        """
        get group point cloud
        return:
            pointCloudData: dictionary -> pointCloudData{
                'vertex': point cloud list
                'color': point cloud color list
            }
        """
        minLengthPoint = np.amin(self.LengthPointCloud)
        coordinates = []
        color = []

        for index in range(len(self.groupPointCloud)):
            coordinatesAux = np.array(self.groupPointCloud[index])
            colorAux = np.array(self.groupColorPointCloud[index])
            coordinates.append(coordinatesAux[0:minLengthPoint, :])
            color.append(colorAux[0:minLengthPoint, :])

        pointCloudData = {
            'vertex': coordinates,
            'color': color
        }
        return pointCloudData

    def getColorPointCloudWidget(self):
        """
        docstring
        """

        #intrinsicMatrix, homograhpyR2D, homograhpyT2D = self.configTransformation()
        #self.transformation.setIntrinsicMatrix(intrinsicMatrix)
        #self.transformation.setHomographyRgbToDepth(homograhpyR2D)
        #self.transformation.setHomographyThermalToRgb(homograhpyT2D)

        self.transformation.setDepthData(self.captureDepthData)
        depthPoint = self.window.horizontalSliderDepth.value()
        vertexPointCloud = self.transformation.depth2xyz(depthPoint / 10)
        colorImagePoint = self.transformation.getColor()

        pointCloud = PointCloud2()
        #config point cloud
        valueClean =  float(self.window.lineEditCleanPoint.text())
        radioPoint = float(self.window.lineEditRadioPoint.text())
        Nneighbors = int(self.window.lineEditNneighbor.text())
        pointCloud.setConfigration(
            self.filterKn, Nneighbors, self.filterClean, valueClean, radioPoint)

        pointCloud.setVertex(vertexPointCloud)
        pointCloud.setColorPointCloud(colorImagePoint)

        widgetPointCloud = pointCloud.getColorPointCloudWidget()

        NPoints = pointCloud.NPoints()
        self.window.labelNpoints.setText(str(NPoints))

        self.pointCloud = pointCloud.getPointCloud()
        self.pointCloudVedo = pointCloud.getPointCloudVedo()
        return widgetPointCloud

    def getPointCloudWidget(self):
        """
        docstring
        """
        self.transformation.setDepthData(self.captureDepthData)

        depthPoint = self.window.horizontalSliderDepth.value()
        vertexPointCloud = self.transformation.depth2xyz(depthPoint / 10)

        pointCloud = PointCloud2()
        #config point cloud
        valueClean = float(self.window.lineEditCleanPoint.text())
        Nneighbors = int(self.window.lineEditNneighbor.text())
        radioPoint = radioPoint = float(self.window.lineEditRadioPoint.text())
        pointCloud.setConfigration(
            self.filterKn, Nneighbors, self.filterClean, valueClean, radioPoint)

        pointCloud.setVertex(vertexPointCloud)


        widgetPointCloud = pointCloud.getPointCloudWidget()

        NPoints = pointCloud.NPoints()
        self.window.labelNpoints.setText(str(NPoints))

        self.pointCloud = pointCloud.getPointCloud()
        self.pointCloudVedo = pointCloud.getPointCloudVedo()
        return widgetPointCloud

    def getHistogram(self):
        """
        docstring
        """
        analyzer = Analyzer()
        analyzer.setImageToAnalyzer(self.captureThermal)
        #analyzer.setImageToAnalyzer(self.colorImagePointCloud)
        analyzer.histograma()

    def startRegister(self):
        """
        docstring
        """
        registration = Registration()
        groupPointCloud = self.getGroupPointCloud()
        registration.setPointCloud(groupPointCloud)
        alignPoint = registration.initICP()
        
        self.vertexAlign = alignPoint['pointCloud']
        color = alignPoint['color']

        pointCloud = PointCloud2()
        #config point cloud
        valueClean =  float(self.window.lineEditCleanPoint.text())
        radioPoint = float(self.window.lineEditRadioPoint.text())
        Nneighbors = int(self.window.lineEditNneighbor.text())
        pointCloud.setConfigration(
            self.filterKn, Nneighbors, self.filterClean, valueClean, radioPoint)

        pointCloud.setVertex(self.vertexAlign)
        pointCloud.setColorPointCloud(color)

        if self.colorRegister == 'colorless':
            widgetPointCloud = pointCloud.getPointCloudWidget()
        else:
            widgetPointCloud = pointCloud.getColorPointCloudWidget()

        NPoints = pointCloud.NPoints()
        self.window.labelNpoints.setText(str(NPoints))

        return widgetPointCloud

    def getPointCloudRegister(self):
        """
        docstring
        """
        vertexPointCloud = self.vertexAlign

        colorImagePoint = self.transformation.getColor()

        pointCloud = PointCloud2()
        #config point cloud
        valueClean = float(self.window.lineEditCleanPoint.text())
        radioPoint = float(self.window.lineEditRadioPoint.text())
        Nneighbors = int(self.window.lineEditNneighbor.text())
        pointCloud.setConfigration(
            self.filterKn, Nneighbors, self.filterClean, valueClean, radioPoint)

        pointCloud.setVertex(vertexPointCloud)
        pointCloud.setColorPointCloud(colorImagePoint)

        #pointCloud.getColorPointCloudWidget()
        widgetPointCloud = pointCloud.getColorPointCloudWidget()

        NPoints = pointCloud.NPoints()
        self.window.labelNpoints.setText(str(NPoints))

        self.pointCloud = pointCloud.getPointCloud()
        self.pointCloudVedo = pointCloud.getPointCloudVedo()

        #self.close_window(widgetPointCloud)
        return widgetPointCloud

    def clickBoxMaxThreshold(self, state):
        if state == QtCore.Qt.Checked:
            self.maxThreshold = True
        else:
            self.maxThreshold = False

    def clickBoxMinThreshold(self, state):
        if state == QtCore.Qt.Checked:
            self.minThreshold = True
        else:
            self.minThreshold = False

    def clickBoxFilter(self, state):
        if state == QtCore.Qt.Checked:
            self.filterKn = True
        else:
            self.filterKn = False

    def clickBoxClean(self, state):
        if state == QtCore.Qt.Checked:
            self.filterClean = True
        else:
            self.filterClean = False

    def pixMapRgbCamera(self, frameRgbCamera):
        frameRgbCamera = self.imageResize(frameRgbCamera, self.scalaImage)
        imageRgbCamera = QtGui.QImage(
            frameRgbCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmapRgb = QtGui.QPixmap.fromImage(imageRgbCamera)
        self.imagePixmapItem1.setPixmap(self.imagePixmapRgb)

    def pixMapDepthCamera(self, frameDepthCamera):
        frameDepthCamera = self.imageResize(
            frameDepthCamera, self.scalaImage)
        imageCamera2 = QtGui.QImage(
            frameDepthCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imageDepthPixmap = QtGui.QPixmap.fromImage(imageCamera2)
        self.imagePixmapItemDepth.setPixmap(self.imageDepthPixmap)

    def pixMapThermalCamera(self, frameThermalCamera):
        frameThermalCamera = self.imageResize(
            frameThermalCamera, self.scalaImage)
        imageRgbCamera = QtGui.QImage(
            frameThermalCamera, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imagePixmapThermal = QtGui.QPixmap.fromImage(imageRgbCamera)
        self.imagePixmapItemThermal.setPixmap(self.imagePixmapThermal)


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

    def getCaptureImages(self):
        return self.captureRgbImage, self.captureDepthData, self.captureThermal

    def imageToQtWidget(self, frame, dimension):
        image = QtGui.QImage(frame, *dimension,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        imagePixmap = QtGui.QPixmap.fromImage(image)
        imageScene = QtWidgets.QGraphicsScene()
        framePixmap = QtGui.QPixmap(*dimension)
        imagePixmapItem = imageScene.addPixmap(framePixmap)
        imagePixmapItem.setPixmap(imagePixmap)
        viewCamera = QtWidgets.QGraphicsView()
        viewCamera.setScene(imageScene)
        return viewCamera

    def saveAllData(self):
        saveData = SaveData(self.window)
        saveData.saveDialog()
        saveData.saveRgbImage(self.captureRgbImage)
        saveData.saveDepthImage(self.captureDepthImage)
        saveData.saveThermalImage(self.captureThermal)
        saveData.saveDepthData(self.captureDepthData)
        saveData.saveRgbThermalImage(self.colorImagePointCloud)
        saveData.savePointCloud(self.pointCloud, self.pointCloudVedo)

    def getPointCloud(self):
        return self.pointCloud

    def getImagesInspection(self):
        imagesInspection = []
        imagesInspection.append(self.captureRgbImage)
        imagesInspection.append(self.captureDepthImage)
        imagesInspection.append(self.captureThermal)
        imagesInspection.append(self.colorImagePointCloud)
        return imagesInspection

    def imageToString(self, img):
        imgBytes = cv2.imencode('.png', img)[1]
        pngStr = base64.b64encode(imgBytes)
        return pngStr

    def cleanAcquisition(self):
        self.clearWorkspace()

        self.counterAcqData = 0
        self.groupDepthData = []
        self.groupRgbImage = []
        self.groupPointCloud = []
        self.groupColorPointCloud = []
        self.LengthPointCloud = []
        #self.colorImagePointCloud = []
        #self.captureDepthData = []
        #self.captureDepthImage = []
        #self.captureRgbImage = []
        #self.captureThermal = []
        #self.pointCloud = {}
        #self.pointCloudVedo = None
        self.window.labelCloudCaptured.setText('0')
        self.window.labelNpoints.setText('0')

        
        

    def clearWorkspace(self):
        for index in reversed(range(self.window.layoutCameras.count())):
            layoutItem = self.window.layoutCameras.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutCameras.removeWidget(widgetToRemove)
        for index in reversed(range(self.window.layoutPointCloudCamera.count())):
            layoutItem = self.window.layoutPointCloudCamera.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutPointCloudCamera.removeWidget(widgetToRemove)
