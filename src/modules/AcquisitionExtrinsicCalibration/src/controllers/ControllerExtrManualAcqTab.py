from PySide2 import QtWidgets
from EventsExtrManualAcquisition import EventsExtrManualAcquisition

class ControllerExtrManualAcqTab():
    """ 
    Controller for manual extrinsic acquisition 
    """

    def __init__(self, window):
        super(ControllerExtrManualAcqTab).__init__()
        self.window = window
        self.eventRgbCamera = EventsExtrManualAcquisition()
        self.eventDepthCamera = EventsExtrManualAcquisition()
        self.eventThermalCamera = EventsExtrManualAcquisition()

    def handlerTurnOnRGBCamera(self):
        rgbImage = self.eventRgbCamera.turnOnCamera('RGB')
        self.window.displayManual.addWidget(rgbImage)

    def handlerTurnOnDepthCamera(self):
        self.whichCameras = 1
        depthImage = self.eventDepthCamera.turnOnCamera('DEPTH')
        self.window.displayManual.addWidget(depthImage)

    def handlerTurnOnThermalCamera(self):
        self.whichCameras = 2
        thermalImage = self.eventThermalCamera.turnOnCamera('THERMAL')
        self.window.displayManual.addWidget(thermalImage)

    def handlerCaptureRGBImage(self):
        rgbImage = self.eventRgbCamera.captureImage('RGB')
        self.window.displayManual.addWidget(rgbImage)

    def handlerCaptureDepthmage(self):
        depthImage = self.eventDepthCamera.captureImage('DEPTH')
        self.window.displayManual.addWidget(depthImage)

    def handlerCaptureThermalImage(self):
        thermalImage = self.eventThermalCamera.captureImage('THERMAL')
        self.window.displayManual.addWidget(thermalImage)
        
    def handlerSaveRgbAndDepthImage(self):
        nameImage = self.saveDialog()
        self.eventRgbCamera.saveImage('RGB',"%sRgb.png" % nameImage)
        self.eventDepthCamera.saveImage('DEPTH', "%sDepth.png" % nameImage)

    def handlerSaveRgbAndThermalImage(self):
        nameImage = self.saveDialog()
        self.eventRgbCamera.saveImage('RGB', "%sRgb.png" % nameImage)
        self.eventThermalCamera.saveImage('THERMAL', "%sThermal.png" % nameImage)

    def handlerTurnOffCamera(self):
        if self.whichCameras == 1:
            self.eventRgbCamera.turnOffCamera()
            self.eventDepthCamera.turnOffCamera()
        if self.whichCameras == 2:
            self.eventRgbCamera.turnOffCamera()
            self.eventThermalCamera.turnOffCamera()

    def saveDialog(self):
        relativePath = 'modules/AcquisitionExtrinsicCalibration/data/images'
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', relativePath, selectedFilter='*.png')
        nameImage = nameImage[0]
        return nameImage
