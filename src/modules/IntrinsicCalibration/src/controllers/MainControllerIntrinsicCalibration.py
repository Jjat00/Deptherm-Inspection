from HandlerIntrinsicCalibration import HandlerIntrinsicCalibration

class MainControllerIntrinsicCalibration():
    """
    docstring
    """
    def __init__(self, mainWidget, intrinsicCalibrationWidget):
        super(MainControllerIntrinsicCalibration).__init__()
        self.mainWidget = mainWidget
        self.window = intrinsicCalibrationWidget.window
        #intrinsicCalibrationWidget.show()
        self.connectButtons()
        intrinsicCalibrationWidget.exec()

    def connectButtons(self):
        self.handler = HandlerIntrinsicCalibration(self.mainWidget, self.window)

        self.window.loadButton.clicked.connect(
            self.handler.handlerLoadPatternImages)

        self.window.startButton.clicked.connect(
            self.handler.handlerStartCalibration)

        self.window.saveButton.clicked.connect(
            self.handler.handlerSaveParameters)

        self.window.previusButton.clicked.connect(
            self.handler.handlerPreviousImage)

        self.window.nextButton.clicked.connect(
            self.handler.handlerNextImage)

        self.window.clearButton.clicked.connect(
            self.handler.handlerClearWorkspace)

        self.window.buttonUploadCloud.clicked.connect(
            self.handler.handlerUploadParameters)
