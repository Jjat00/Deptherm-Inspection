from EventsExtrinsicCalibration import EventsExtrinsicCalibration
from CalibrationDB import *
from PySide2 import QtWidgets
import glob
import json

class HandlerExtrinsicCalibration():
    def __init__(self, mainWindow, window):
        super(HandlerExtrinsicCalibration).__init__()
        self.mainWindow = mainWindow
        self.window = window
        self.action = EventsExtrinsicCalibration(self.window)
        self.whichImage = 0
        self.loadPatter = False
        self.save = False

    def handlerLoadPatternImages(self):
        pathImagesSrc = self.action.selectDirectoryImages()
        pathImagesDst = self.action.selectDirectoryImages()
        if pathImagesSrc != '' and pathImagesDst != '':
            self.patternImagesSrc = glob.glob(pathImagesSrc+"/*.png")
            self.patternImagesDst = glob.glob(pathImagesDst+"/*.png")
            self.totalImagesCalibration = len(self.patternImagesSrc)
            self.action.showImage(self.patternImagesSrc[0])
            self.action.showImage(self.patternImagesDst[0])
            self.loadPatter = True
            self.showNoCurrentImage()

    def handlerStartCalibration(self):
        if self.loadPatter:
            self.action.startExtrinsicCalibration(
                self.patternImagesSrc, self.patternImagesDst)
            self.patternImagesSrc, self.patternImagesDst = self.action.getPatternImages()
            self.save = True
            self.whichImage = 0
            self.showNoCurrentImage()

    def handlerSaveParameters(self):
        if self.save:
            self.action.saveDialog()

    def handlerClearWorkspace(self):
        self.action.clearWorkspace()
        self.action.resetParameters()
        self.loadPatter = False
        self.save = False
        self.patternImagesSrc = []
        self.patternImagesDst = []
        self.whichImage = 0
        self.window.currentImageLabel.setText('0 / 0')
        self.window.progressBarExtsc.setValue(0)

    def handlerPreviousParameters(self):
        if self.loadPatter:
            if (self.whichImage > 0):
                self.action.clearWorkspace()
                self.whichImage = self.whichImage - 1
                self.action.showImage(
                    self.patternImagesSrc[self.whichImage])
                self.action.showImage(
                    self.patternImagesDst[self.whichImage])
                self.showNoCurrentImage()

    def handlerNextParameters(self):
        if self.loadPatter:
            if (self.whichImage < self.totalImagesCalibration-1):
                self.action.clearWorkspace()
                self.whichImage = self.whichImage + 1
                self.action.showImage(
                    self.patternImagesSrc[self.whichImage])
                self.action.showImage(
                    self.patternImagesDst[self.whichImage])
                self.showNoCurrentImage()

    def showNoCurrentImage(self):
        self.currentImage = str(self.whichImage) + \
            ' / ' + str(self.totalImagesCalibration-1)
        self.window.currentImageLabel.setText(self.currentImage)

    def uploadData(self):
        print('helloooo')
        homographyMatrix = self.action.getHomographyMatrix()
        paramFocales = json.dumps({'matriz': []})
        paramDistortion = json.dumps({'matriz': []})
        matrizHomografia = json.dumps(homographyMatrix)
        print("matrizHomografia")
        print(matrizHomografia)
        camera = str(self.window.comboBox.currentText())
        print('camera')
        print(camera)
        idUsuario = self.mainWindow.user.getUserID()
        print(idUsuario)

        message = QtWidgets.QMessageBox.question(
            self.window, "Choice message", "You are sequre?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if message == QtWidgets.QMessageBox.Yes:
            res = insertCalibration(camera, idUsuario, 2,
                        paramFocales, paramDistortion, matrizHomografia)
            self.uploadImages()
            if res == 200:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload successful")
            else:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload failed,\n id calibrarion alredy exist")

    def uploadImages(self):
        import cv2
        import base64
        imagesSrc, imagesDst = self.action.getImagesCalibration()
        idCalibration = int(getLastCalib())
        self.window.progressBarExtsc.setValue(0)
        NoImages = len(imagesSrc)
        for index in range(NoImages):
            imgSrcBytes = cv2.imencode('.png', imagesSrc[index])[1]
            pngSrcStr = base64.b64encode(imgSrcBytes)

            imgDstBytes = cv2.imencode('.png', imagesDst[index])[1]
            pngDstStr = base64.b64encode(imgDstBytes)

            res = insertImages(idCalibration, pngSrcStr, pngDstStr)
            value = (index / NoImages) * 100
            self.window.progressBarExtsc.setValue(value)
            print(res)
