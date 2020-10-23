from PySide2 import QtWidgets
from EventsAcquisitionAllCam import EventsAcquisitionAllCam


class HandlerAcquisitionCameras():
    """ 
    Controller for automatic acquisition  all cameras
    """

    def __init__(self, window):
        super(HandlerAcquisitionCameras).__init__()
        self.window = window
        self.event = EventsAcquisitionAllCam(self.window)
        self.clickTurnOn = False
        self.startAcq = False

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        period = float(self.window.period.text())
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.event.setConfigAutoAcq(NoImages, period, self.pathImages)

    def handlerTurnOnCameras(self):
        rgbFrame, depthFrame, thermalFrame = self.event.turnOnCameras()
        self.window.displayAuto.addWidget(rgbFrame)
        self.window.displayAuto.addWidget(depthFrame)
        self.window.displayAuto.addWidget(thermalFrame)
        self.clickTurnOn = True

    def handlerStartImagesAcq(self):
        self.startAcq = True
        if self.clickTurnOn:
            self.configAdqcquisition()
            if self.pathImages != '':
                print("start save images")
                self.event.startSaveImages()
            self.clickTurnOn = False

    def handlerStopAcquisition(self):
        if self.clickTurnOn or self.startAcq:
            self.event.turnOffCamera()
            self.clickTurnOn = False

    def saveDialog(self):
        relativePath = 'modules/AcquisitionAllCameras/data/images'
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.png')
        return pathImages
