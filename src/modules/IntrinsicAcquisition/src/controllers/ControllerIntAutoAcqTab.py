from PySide2 import QtWidgets
from EventsIntAutoAcquisition import EventsIntAutoAcquisition

class ControllerIntAutoAcqTab():
    """ 
    Controller for automatic intrinsic acquisition 
    """
    
    def __init__(self, window):
        super(ControllerIntAutoAcqTab).__init__()
        self.window = window
        self.event = EventsIntAutoAcquisition(self.window)

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        periodAcq = float(self.window.periodAcq.text())
        patternDimension = (int(self.window.cornerX.text()), int(self.window.cornerY.text()))
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.event.setConfigAutoAcq(NoImages, periodAcq, patternDimension, self.pathImages)

    def handlerStartRgbImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('RGB')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartDepthImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('DEPTH')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartThermalImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('THERMAL')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStopAcquisition(self):
        self.event.turnOffCamera()

    def saveDialog(self):
        relativePath = 'modules/IntrinsicAcquisition/data/images'
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.png')
        return pathImages
