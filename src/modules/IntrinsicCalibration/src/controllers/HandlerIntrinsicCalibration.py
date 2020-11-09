from EventsIntrinsicCalibration import EventsIntrinsicCalibration
from PySide2 import QtWidgets
import urlfetch
import json
import glob
from CalibrationDB import insertCalibration, insertImage

class HandlerIntrinsicCalibration():
    def __init__(self, mainWindow, window):
        super(HandlerIntrinsicCalibration).__init__()
        self.mainWindow = mainWindow
        self.window = window
        self.event = EventsIntrinsicCalibration(self.window)
        self.whichImage = 0
        self.loadPatter = False
        self.save = False

    def handlerLoadPatternImages(self):
        pathImages = self.event.selectDirectoryImages()
        if pathImages != '':
            self.patternImages = glob.glob(pathImages+"/*.png")
            self.totalImagesCalibration = len(self.patternImages)
            self.event.showImage(self.patternImages[0])
            self.loadPatter = True
            self.showCurrentImage()

    def handlerStartCalibration(self):
        if self.loadPatter:
            self.event.startIntrinsicCalibration(self.patternImages)
            self.patternImages = self.event.getPatternImage()
            self.save = True
            self.whichImage = 0
            self.showCurrentImage()

    def handlerSaveParameters(self):
        if self.save:
            self.event.saveDialog()

    def handlerClearWorkspace(self):
        self.event.clearWorkspace()
        self.event.resetParameters()
        self.loadPatter = False
        self.save = False
        self.patternImages = []
        self.whichImage = 0
        self.window.currentImageLabel.setText('0 / 0')
        self.window.progressBarIntrsc.setValue(0)

    def handlerPreviousImage(self):
        if self.loadPatter:
            if (self.whichImage > 0):
                self.event.clearWorkspace()
                self.whichImage = self.whichImage - 1
                self.event.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def handlerNextImage(self):
        if self.loadPatter:
            if (self.whichImage < self.totalImagesCalibration-1):
                self.event.clearWorkspace()
                self.whichImage = self.whichImage + 1
                self.event.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def handlerUploadParameters(self):
        parameters = self.event.getParameters()
        paramFocales = json.dumps(parameters['focalParameters'])
        paramDistortion = json.dumps(parameters['distortionParameters'])
        matrizHomografia = json.dumps({'matriz': []})

        idUsuario = self.mainWindow.user.getUserID()
        id = int(self.window.lineEditIDcalib.text())

        message = QtWidgets.QMessageBox.question(
            self.window, "Choice message", "You are sequre?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if message == QtWidgets.QMessageBox.Yes:
            res = insertCalibration(id, idUsuario, 1,
                          paramFocales, paramDistortion, matrizHomografia)
            self.uploadImages()
            if res == 200:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload successful")
            else:
                message = QtWidgets.QMessageBox.about(
                    self.window, "About aplication", "calibration upload failed,\n id calibrarion alredy exist")

    def uploadImages(self):
        imagesStr = self.event.getImagesCalibration()
        name = self.window.lineEditNameCalib.text()
        idCalibration = int(self.window.lineEditIDcalib.text())
        self.window.progressBarIntrsc.setValue(0)
        NoImages = len(imagesStr)
        for index in range(NoImages):
            res = insertImage("%s%i" % (name, index),
                              idCalibration, imagesStr[index])
            value = (index / NoImages) * 100
            self.window.progressBarIntrsc.setValue(value)                              
            print(res)

    def showCurrentImage(self):
        self.currentImage = str(self.whichImage) + \
            ' / ' + str(self.totalImagesCalibration-1)
        self.window.currentImageLabel.setText(self.currentImage)
