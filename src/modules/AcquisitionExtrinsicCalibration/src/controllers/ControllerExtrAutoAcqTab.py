from PySide2 import QtWidgets
from EventsExtrAutoAcquisition import EventsExtrAutoAcquisition

class ControllerExtrAutoAcqTab():
    """ 
    Controller for automatic extrinsic acquisition 
    """

    def __init__(self, window):
        super(ControllerExtrAutoAcqTab).__init__()
        self.window = window
        self.event = EventsExtrAutoAcquisition(self.window)

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        periodAcq = float(self.window.periodAcq.text())
        patternDimension = (int(self.window.cornerX.text()),
                            int(self.window.cornerY.text()))
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.event.setConfigAutoAcq(
                NoImages, periodAcq, patternDimension, self.pathImages)

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
        relativePath = 'modules/AcquisitionExtrinsicCalibration/data/images'
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.png')
        return pathImages
