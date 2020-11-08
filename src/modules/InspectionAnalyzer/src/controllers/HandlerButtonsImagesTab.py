from ControllerManualFusion import ManualFusion

class HandlerButtonsImagesTab():
    def __init__(self, window):
        print('init HandlerButtonsImagesTab')
        self.window = window
        self.controllerFusion = ManualFusion(self.window)

    def connectButtonLoadRgbImage(self):
        self.window.buttonLoadRgb.clicked.connect(
            self.controllerFusion.loadRgbImage)

    def connectButtonLoadDepthImage(self):
        self.window.buttonLoadDepth.clicked.connect(
            self.controllerFusion.loadDepthImage)

    def connectButtonLoadThremalImage(self):
        self.window.buttonLoadThermal.clicked.connect(
            self.controllerFusion.loadThermalImage)

    def connectButtonDepthToCloud(self):
        try:
            self.window.buttonShowPointImages.clicked.disconnect()
            self.depthToCloud()
        except:
            self.depthToCloud()

    def depthToCloud(self):
        self.window.buttonShowPointImages.clicked.connect(
            self.controllerFusion.showPointCloud)

    def connectButtonDepthToColorCloud(self):
        try:
            self.window.buttonShowPointImages.clicked.disconnect()
            self.depthToColorCloud()
        except:
            self.depthToColorCloud()

    def depthToColorCloud(self):
        self.window.buttonShowPointImages.clicked.connect(
            self.controllerFusion.showColorPointCloud)

    def connectButtonDepthToThermalCloud(self):
        try:
            self.window.buttonShowPointImages.clicked.disconnect()
            self.depthToThermalCloud()
        except:
            self.depthToThermalCloud()

    def depthToThermalCloud(self):
        self.window.buttonShowPointImages.clicked.connect(
            self.controllerFusion.showThermalPointCloud)


    def connectButtonDepthToRgbThermalCloud(self):
        try:
            self.window.buttonShowPointImages.clicked.disconnect()
            self.depthToRgbThermalCloud()
        except:
            self.depthToRgbThermalCloud()

    def depthToRgbThermalCloud(self):
        pass
