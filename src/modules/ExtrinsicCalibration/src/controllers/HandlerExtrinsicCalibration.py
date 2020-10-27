from PySide2 import *
import glob
from EventsExtrinsicCalibration import EventsExtrinsicCalibration

class HandlerExtrinsicCalibration():
    def __init__(self, window):
        super(HandlerExtrinsicCalibration).__init__()
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
