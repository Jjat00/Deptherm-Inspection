from ControllerAcquisitionInspection import ControllerAcquisitionInspection
from PointCloudDB import insertPointCloud, insertImagesCloud
from PySide2 import QtWidgets
import json
import sys

class ControllerCamerasTab():
    def __init__(self, window):
        print('init ControllerCamerasTab')
        self.window = window
        self.controllerAcquisition = ControllerAcquisitionInspection(
            self.window)

    def __del__(self):
        print('delete ControllerCamerasTab')

    def handlerTurnOnCameras(self):
        self.controllerAcquisition.cleanAcquisition()
        self.window.buttonUpload.setEnabled(False)
        frameRgb, frameDepth, frameThermal = self.controllerAcquisition.turnOnCameras()
        self.window.layoutCameras.addWidget(frameDepth)
        self.window.layoutCameras.addWidget(frameRgb)
        self.window.layoutCameras.addWidget(frameThermal)

    def handlerCaptureImages(self):
        self.clearWorkspace()
        numerImages = self.window.numberImages.text()
        self.controllerAcquisition.captureImage(numerImages)
        frameDepth = self.controllerAcquisition.getDepthImageWidget()
        self.window.layoutPointCloudCamera.addWidget(frameDepth)
        self.enableButtons()

    def handlerShowRgbImage(self):
        """
        docstring
        """
        self.clearWorkspace()
        rgbImageWidget = self.controllerAcquisition.getRgbImageWidget()
        self.window.layoutPointCloudCamera.addWidget(rgbImageWidget)

    def handlerShowDepthImage(self):
        """
        docstring
        """
        self.clearWorkspace()
        depthImage = self.controllerAcquisition.getDepthImageWidget()
        self.window.layoutPointCloudCamera.addWidget(depthImage)

    def handlerShowThermalImage(self):
        """
        docstring
        """
        self.clearWorkspace()
        themalImageWidget = self.controllerAcquisition.getThermalImageWidget()
        self.window.layoutPointCloudCamera.addWidget(themalImageWidget)

    def handlerShowThermalRgbImage(self):
        """
        docstring
        """
        self.clearWorkspace()
        thermalRgbImageWidget = self.controllerAcquisition.getThermalRGBWidget()
        self.window.layoutPointCloudCamera.addWidget(thermalRgbImageWidget)

    def handlerShowRgbDepthImage(self):
        """
        docstring
        """
        self.clearWorkspace()
        rgbDepthImageWidget = self.controllerAcquisition.getDepthRgbImageWidget()
        self.window.layoutPointCloudCamera.addWidget(rgbDepthImageWidget)

    def handlerShowHistogram(self):
        """
        docstring
        """
        self.controllerAcquisition.getHistogram()

    def handlerStartICPRegistration(self):
        """
        init icp registration
        """
        widgetPointCloud = self.controllerAcquisition.startRegister()
        self.clearWorkspace()
        self.window.layoutPointCloudCamera.addWidget(widgetPointCloud)

    def handlerShowPointCloudRegister(self):
        """
        docstring
        """
        self.clearWorkspace()
        self.window.buttonUpload.setEnabled(True)
        widgetPointCloud = self.controllerAcquisition.getPointCloudRegister()
        self.window.layoutPointCloudCamera.addWidget(widgetPointCloud)

    def handlerShowPointCloud(self):
        self.clearWorkspace()
        self.window.buttonUpload.setEnabled(True)
        widgetPointCloud = self.controllerAcquisition.getPointCloudWidget()
        self.window.layoutPointCloudCamera.addWidget(widgetPointCloud)

    def handlerShowColorPointCloud(self):
        self.clearWorkspace()
        self.window.buttonUpload.setEnabled(True)
        widgetPointCloud = self.controllerAcquisition.getColorPointCloudWidget()
        self.window.layoutPointCloudCamera.addWidget(widgetPointCloud)

    def handlerUploadData(self):
        message = QtWidgets.QMessageBox.question(
            self.window, "Choice message", "You are sequre?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if message == QtWidgets.QMessageBox.Yes:
            idCloud = int(self.window.lineEditIDCloud.text())
            pointCloud = self.controllerAcquisition.getPointCloud()
            vertex = {
                'vertex': pointCloud['vertex']
            }
            colorPointCloud = {
                'color': pointCloud['color']
            }
            res = insertPointCloud(idCloud, json.dumps(vertex), json.dumps(colorPointCloud))
            print(res)
            imagesPointCloud = self.controllerAcquisition.getImagesInspection()
            rgbImage = self.controllerAcquisition.imageToString(imagesPointCloud[0])
            depthImage = self.controllerAcquisition.imageToString(imagesPointCloud[1])
            thermalImage = self.controllerAcquisition.imageToString(imagesPointCloud[2])
            colorImage = self.controllerAcquisition.imageToString(imagesPointCloud[3])
            res = insertImagesCloud(idCloud, rgbImage, depthImage, thermalImage, colorImage)
            print(res)
            if res == 200:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload successful")
            else:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload failed,\n id calibrarion alredy exist")

    def handlerCleanWorkspace(self):
        self.controllerAcquisition.cleanAcquisition()
        self.clearWorkspace()

    def handlerSaveData(self):
        self.controllerAcquisition.saveAllData()

    def clearWorkspace(self):
        #self.controllerAcquisition.cleanAcquisition()
        for index in reversed(range(self.window.layoutPointCloudCamera.count())):
            layoutItem = self.window.layoutPointCloudCamera.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layoutPointCloudCamera.removeWidget(widgetToRemove)

    def enableButtons(self):
        """
        docstring
        """
        self.window.buttonClean.setEnabled(True)
        self.window.buttonShowPointCamera.setEnabled(True)
        self.window.buttonSavePointCloud.setEnabled(True)

        self.window.showDepth.setEnabled(True)
        self.window.showRgbDepth.setEnabled(True)
        self.window.showRGB.setEnabled(True)
        self.window.showThermal.setEnabled(True)
        self.window.showThermalRgb.setEnabled(True)
        self.window.buttonHistogram.setEnabled(True)
        self.window.buttonStartICP.setEnabled(True)
        self.window.buttonShowPointRegister.setEnabled(True)
