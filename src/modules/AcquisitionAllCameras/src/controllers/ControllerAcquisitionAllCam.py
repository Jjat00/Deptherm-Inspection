from HandlerAcquisitionCameras import HandlerAcquisitionCameras

class ControllerAcquisitionAllCam():
    """
    Main controller for extrínsic acquisition Qtwidget
    """

    def __init__(self, acquisitionAllCameras):
        super(ControllerAcquisitionAllCam).__init__()
        self.window = acquisitionAllCameras.window
        self.connectButtonsAutomaticAcquisition()
        acquisitionAllCameras.exec()


    def connectButtonsAutomaticAcquisition(self):
        """ 
        Connect  and disconnect buttons automatic acquisition tab and clean workspace every
        time the camera is changed
        """
        self.controllerAutoAcq = HandlerAcquisitionCameras(self.window)

        self.window.onButtonAuto.clicked.connect(
            self.controllerAutoAcq.handlerTurnOnCameras)
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartImagesAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)


    def disconnectButtons(self):
        """
        Disconnect buttons automatic acquisition
        """
        self.window.startButton.clicked.disconnect()
        self.window.stopButton.clicked.disconnect()
