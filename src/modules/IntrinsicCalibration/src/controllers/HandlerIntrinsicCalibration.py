from EventsIntrinsicCalibration import EventsIntrinsicCalibration
from PySide2 import *
import glob


class HandlerIntrinsicCalibration():
    def __init__(self, window):
        super(HandlerIntrinsicCalibration).__init__()
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

    def handlerPreviousParameters(self):
        if self.loadPatter:
            if (self.whichImage > 0):
                self.event.clearWorkspace()
                self.whichImage = self.whichImage - 1
                self.event.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def handlerNextParameters(self):
        if self.loadPatter:
            if (self.whichImage < self.totalImagesCalibration-1):
                self.event.clearWorkspace()
                self.whichImage = self.whichImage + 1
                self.event.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def showCurrentImage(self):
        self.currentImage = str(self.whichImage) + \
            ' / ' + str(self.totalImagesCalibration-1)
        self.window.currentImageLabel.setText(self.currentImage)
