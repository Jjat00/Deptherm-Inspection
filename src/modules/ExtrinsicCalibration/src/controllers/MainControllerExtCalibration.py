from HandlerExtrinsicCalibration import HandlerExtrinsicCalibration

class MainControllerExtCalibration():
    """
    Controller for extrinsic camera calibration
    """

    def __init__(self, extrinsicCalibWidget):
        super(MainControllerExtCalibration).__init__()
        self.window = extrinsicCalibWidget.window
        self.connectButtons()
        extrinsicCalibWidget.exec()

    def connectButtons(self):
        """
        connect all buttons
        """
        self.handler = HandlerExtrinsicCalibration(self.window)

        self.window.loadButton.clicked.connect(
            self.handler.handlerLoadPatternImages)

        self.window.startButton.clicked.connect(
            self.handler.handlerStartCalibration)

        self.window.saveButton.clicked.connect(
            self.handler.handlerSaveParameters)

        self.window.previusButton.clicked.connect(
            self.handler.handlerPreviousParameters)

        self.window.nextButton.clicked.connect(
            self.handler.handlerNextParameters)

        self.window.clearButton.clicked.connect(
            self.handler.handlerClearWorkspace)
