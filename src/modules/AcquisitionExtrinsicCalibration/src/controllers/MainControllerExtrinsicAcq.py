from ControllerAutoAcqTab import ControllerAutoAcqTab
from ControllerManualAcqTab import ControllerManualAcqTab

class MainControllerExtrinsicAcq():
    """
    Main controller for extrínsic acquisition Qtwidget
    """

    def __init__(self, extrinsicAcquisitionWidget):
        super(MainControllerExtrinsicAcq).__init__()
        self.window = extrinsicAcquisitionWidget.window
        self.connectComboBoxChosenCamera() 
        extrinsicAcquisitionWidget.exec()


    def connectComboBoxChosenCamera(self):
        """
        Connect comboBox chosen camera: RGB, depth or thermal camera
        """
        self.connectButtonsManualAcquisition()
        self.window.comboBoxManual.currentIndexChanged.connect(
            self.connectButtonsManualAcquisition)
        self.connectButtonsAutoAcq()
        self.window.comboBoxAuto.currentIndexChanged.connect(
            self.connectButtonsAutoAcq)


    def connectButtonsManualAcquisition(self):
        """ 
        Connect  and disconnect buttons automatica acquisition tab and clean workspace every
        time the camera is changed
        """
        self.controllerManualAcq = ControllerManualAcqTab(self.window)
        chosenCamera = self.window.comboBoxManual.currentText()
        if chosenCamera == "RGB-DEPTH":
            self.connectButtonsRgbCamera()
            self.connectButtonsDepthCamera()
        if chosenCamera == "RGB-THERMAL":
            self.connectButtonsRgbCamera()
            self.connectButtonsThermalCamera()
        if chosenCamera == "NONE":
            pass

    def connectButtonsRgbCamera(self):
        try:
            self.disconnectButtons()
            self.connectButtonsRgb()
        except:
            self.connectButtonsRgb()

    def connectButtonsDepthCamera(self):
        """
        Connect buttons manual acquisition for depth camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnDepthCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureDepthmage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveRgbAndDepthImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def connectButtonsThermalCamera(self):
        """
        Connect buttons manual acquisition for thermal camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnThermalCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureThermalImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveRgbAndThermalImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def connectButtonsRgb(self):
        """
        Connect buttons manual acquisition for rgb camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnRGBCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureRGBImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def disconnectButtons(self):
        """
        Disconnect buttons manual acquisition
        """
        self.window.onButton.clicked.disconnect()
        self.window.captureButton.clicked.disconnect()
        self.window.saveButton.clicked.disconnect()
        self.window.offButton.clicked.disconnect()


    def connectButtonsAutoAcq(self):
        """ 
        Connect  and disconnect buttons automatic acquisition tab and clean workspace every
        time the camera is changed
        """
        self.controllerAutoAcq = ControllerAutoAcqTab(self.window)
        chosenCamera = self.window.comboBoxAuto.currentText()
        if chosenCamera == "RGB-DEPTH":
            self.connectButtonsRGbAndDepthCamera()
        if chosenCamera == "RGB-THERMAL":
            self.connectButtonsRgbAndThermalCamera()
        if chosenCamera == "NONE":
            pass

    def connectButtonsRGbAndDepthCamera(self):
        """
        Connect buttons automatic acquisition for rgb and depth camera
        """
        try:
            self.disconnectButtons()
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStartRgbAndDepthImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)
        except:
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStartRgbAndDepthImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)

    def connectButtonsRgbAndThermalCamera(self):
        """
        Connect buttons automatic acquisition for rgb and thermal camera
        """
        try:
            self.disconnectButtons()
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStarRgbAndThermalImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)
        except:
            self.window.startButton.clicked.connect(
                self.controllerAutoAcq.handlerStarRgbAndThermalImageAcq)
            self.window.stopButton.clicked.connect(
                self.controllerAutoAcq.handlerStopAcquisition)

    def disconnectButtons(self):
        """
        Disconnect buttons automatic acquisition
        """
        self.window.startButton.clicked.disconnect()
        self.window.stopButton.clicked.disconnect()
