from HandlerIntrinsicCalibration import HandlerIntrinsicCalibration

class MainControllerIntrinsicCalibration():
    """
    docstring
    """
    def __init__(self, intrinsicCalibrationWidget):
        super(MainControllerIntrinsicCalibration).__init__()
        self.window = intrinsicCalibrationWidget.window
        #intrinsicCalibrationWidget.show()
        self.connectButtons()
        intrinsicCalibrationWidget.exec()

    def connectButtons(self):
        self.handler = HandlerIntrinsicCalibration(self.window)

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
