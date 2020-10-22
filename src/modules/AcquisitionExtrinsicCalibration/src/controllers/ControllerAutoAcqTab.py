from PySide2 import QtWidgets
from EventsAutoAcquisition import EventsAutoAcquisition

class ControllerAutoAcqTab():
    """ 
    Controller for automatic extrinsic acquisition 
    """

    def __init__(self, window):
        super(ControllerAutoAcqTab).__init__()
        self.window = window
        self.event = EventsAutoAcquisition(self.window)

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        patternDimension = (int(self.window.cornerX.text()),
                            int(self.window.cornerY.text()))
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.event.setConfigAutoAcq(
                NoImages, patternDimension, self.pathImages)

    def handlerStartRgbAndDepthImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage, depthImage = self.event.turnOnCamera('RGB-DEPTH')
            self.window.displayAuto.addWidget(rgbImage)
            self.window.displayAuto.addWidget(depthImage)

    def handlerStarRgbAndThermalImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage, themalImage = self.event.turnOnCamera('RGB-THERMAL')
            self.window.displayAuto.addWidget(rgbImage)
            self.window.displayAuto.addWidget(themalImage)

    def handlerStopAcquisition(self):
        self.event.turnOffCamera()

    def saveDialog(self):
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        return pathImages
