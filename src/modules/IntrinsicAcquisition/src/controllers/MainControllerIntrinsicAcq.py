from PySide2 import QtWidgets
from ControllerIntAutoAcqTab import ControllerIntAutoAcqTab
from ControllerIntManualAcqTab import ControllerIntManualAcqTab


class MainControllerIntrinsicAcq():
    """
    Main controller app Deptherm Inspection
    """

    def __init__(self, intrinsicAcquisitionWidget):
        super(MainControllerIntrinsicAcq).__init__()
        self.window = intrinsicAcquisitionWidget.window
        self.connectComboBoxChosenCamera()
        intrinsicAcquisitionWidget.exec()

    def connectComboBoxChosenCamera(self):
        """
        Connect comboBox chosen camera: RGB, depth or thermal camera
        """
        self.connectButtonsManualAcquisition()
        self.window.comboBoxManual.currentIndexChanged.connect(
            self.connectButtonsManualAcquisition)
        self.connectButtonsAtomaticAcquisition()
        self.window.comboBoxAuto.currentIndexChanged.connect(
            self.connectButtonsAtomaticAcquisition)

    def connectButtonsManualAcquisition(self):
        """ 
        Connect  and disconnect buttons manual acquisition tab and clean workspace every
        time the camera is changed
        """
        self.controllerManualAcq = ControllerIntManualAcqTab(self.window)
        chosenCamera = self.window.comboBoxManual.currentText()
        if chosenCamera == "RGB":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqRgbCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqRgbCamera()
        if chosenCamera == "DEPTH":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqDepthCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqDepthCamera()
        if chosenCamera == "THERMAL":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqThermalCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqThermalCamera()
        if chosenCamera == "NONE":
            pass

    def buttonsManualAcqRgbCamera(self):
        """
        Connect buttons manual acquisition for rgb camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnRGBCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureRGBImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveRgbImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def buttonsManualAcqDepthCamera(self):
        """
        Connect buttons manual acquisition for depth camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnDepthCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureDepthmage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveDepthImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def buttonsManualAcqThermalCamera(self):
        """
        Connect buttons manual acquisition for thermal camera
        """
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnThermalCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureThermalImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveThermalImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def disconnectButtonsManualAcqTab(self):
        """
        Disconnect buttons manual acquisition
        """
        self.window.onButton.clicked.disconnect()
        self.window.captureButton.clicked.disconnect()
        self.window.saveButton.clicked.disconnect()

    def connectButtonsAtomaticAcquisition(self):
        """ 
        Connect and disconnect buttons automatic acquisition tab and clean workspace every
        time the camera is changed
        """
        self.controllerAutoAcq = ControllerIntAutoAcqTab(self.window)
        chosenCamera = self.window.comboBoxAuto.currentText()
        if chosenCamera == "RGB":
            try:
                self.cleanWorkspaceAutoAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqRgbCamera()
            except:
                self.cleanWorkspaceAutoAcq()
                self.buttonsAutoAcqRgbCamera()
        if chosenCamera == "DEPTH":
            try:
                self.cleanWorkspaceAutoAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqDepthCamera()
            except:
                self.cleanWorkspaceAutoAcq()
                self.buttonsAutoAcqDepthCamera()
        if chosenCamera == "THERMAL":
            try:
                self.cleanWorkspaceAutoAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqThermalCamera()
            except:
                self.cleanWorkspaceAutoAcq()
                self.buttonsAutoAcqThermalCamera()
        if chosenCamera == "NONE":
            pass

    def buttonsAutoAcqRgbCamera(self):
        """
        Connect buttons automatic acquisition for rgb camera
        """
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartRgbImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def buttonsAutoAcqDepthCamera(self):
        """
        Connect buttons automatic acquisition for depth camera
        """
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartDepthImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def buttonsAutoAcqThermalCamera(self):
        """
        Connect buttons automatic acquisition for thermal camera
        """
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartThermalImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def cleanWorkspaceManualAcq(self):
        """
        Clean workspace remove all widget
        """
        for index in reversed(range(self.window.displayManual.count())):
            layoutItem = self.window.displayManual.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: %s" % str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.displayManual.removeWidget(widgetToRemove)

    def cleanWorkspaceAutoAcq(self):
        """
        Clean workspace remove all widget
        """
        for index in reversed(range(self.window.displayAuto.count())):
            layoutItem = self.window.displayAuto.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.displayAuto.removeWidget(widgetToRemove)
