from ControllerCamerasTab import ControllerCamerasTab
from ControllerConfigAnalyzer import ControllerConfigAnalyzer

class HandlerButtonsCamerasTab():
    def __init__(self, window):
        print('init HandlerButtonsCamerasTab')
        self.window = window
        self.controller = ControllerCamerasTab(self.window)
        self.controllerConfig = ControllerConfigAnalyzer(self.window)

    def connectOnButton(self):
        self.window.buttonTurnOn.clicked.connect(
            self.controller.handlerTurnOnCameras)

    def connectCaptureButton(self):
        self.window.buttonCapture.clicked.connect(
            self.controller.handlerCaptureImages)

    def connectShowRGBButton(self):
        """
        docstring
        """
        self.controller.clearWorkspace()
        self.window.showRGB.clicked.connect(self.controller.handlerShowRgbImage)

    def connectShowDepthButton(self):
        """
        docstring
        """
        self.controller.clearWorkspace()
        self.window.showDepth.clicked.connect(
            self.controller.handlerShowDepthImage)

    def connectShowThermalButton(self):
        """
        docstring
        """
        self.controller.clearWorkspace()
        self.window.showThermal.clicked.connect(
            self.controller.handlerShowThermalImage)

    def connectShowThermalRgbButton(self):
        """
        docstring
        """
        self.controller.clearWorkspace()
        self.window.showThermalRgb.clicked.connect(
            self.controller.handlerShowThermalRgbImage)

    def connectShowRgbDepthButton(self):
        """
        docstring
        """
        self.controller.clearWorkspace()
        self.window.showRgbDepth.clicked.connect(
            self.controller.handlerShowRgbDepthImage)

    def connectShowHistogramButton(self):
        """
        docstring
        """
        self.window.buttonHistogram.clicked.connect(
            self.controller.handlerShowHistogram)

    def connectStartICPButton(self):
        self.window.buttonStartICP.clicked.connect(
            self.controller.handlerStartICPRegistration)

    def connectShowRegisterCloud(self):
        """
        docstring
        """
        self.window.buttonShowPointRegister.clicked.connect(
            self.controller.handlerShowPointCloudRegister)

    def connectButtonPointCloud(self):
        try:
            self.window.buttonShowPointCamera.clicked.disconnect()
            self.pointCloud()
        except:
            self.pointCloud()
        
    def pointCloud(self):
        self.window.buttonShowPointCamera.clicked.connect(
            self.controller.handlerShowPointCloud)

    def connectButtonColorPointCloud(self):
        try:
            self.window.buttonShowPointCamera.clicked.disconnect()
            self.colorPointCloud()
        except:
            self.colorPointCloud()

    def colorPointCloud(self):
        self.window.buttonShowPointCamera.clicked.connect(
            self.controller.handlerShowColorPointCloud)

    def connectButtonThermalPointCloud(self):
        try:
            self.window.buttonShowPointCamera.clicked.disconnect()
            self.thermalPointCloud()
        except:
            self.thermalPointCloud()

    def thermalPointCloud(self):
        self.window.buttonShowPointCamera.clicked.connect(
            self.controller.handlerShowThermalPointCloud)

    def connectButtonRgbThermalPointCloud(self):
        try:
            self.window.buttonShowPointCamera.clicked.disconnect()
            self.rgbThermalPointCloud()
        except:
            self.rgbThermalPointCloud()

    def connectCleanButton(self):
        self.window.buttonClean.clicked.connect(
            self.controller.handlerCleanWorkspace)

    def connectbuttonSaveData(self):
        """
        docstring
        """
        self.window.buttonSavePointCloud.clicked.connect(
            self.controller.handlerSaveData)


    def disabledButtuns(self):
        """
        docstring
        """
        self.window.buttonClean.setEnabled(False)
        self.window.buttonShowPointCamera.setEnabled(False)
        self.window.buttonSavePointCloud.setEnabled(False)

        self.window.showDepth.setEnabled(False)
        self.window.showRgbDepth.setEnabled(False)
        self.window.showRGB.setEnabled(False)
        self.window.showThermal.setEnabled(False)
        self.window.showThermalRgb.setEnabled(False)
        self.window.buttonHistogram.setEnabled(False)
        self.window.buttonStartICP.setEnabled(False)
        self.window.buttonShowPointRegister.setEnabled(False)
        self.window.buttonUpload.setEnabled(False)

    def connectUploadData(self):
        self.window.buttonUpload.clicked.connect(
            self.controller.handlerUploadData)

    def ConnectButtonLoadIntrinsic(self):
        """
        docstring
        """
        self.window.buttonLoadIntrinsic.clicked.connect(
            self.controllerConfig.loadIntrinsicMatrix)

    def ConnectButtonLoadHomography1(self):
        """
        docstring
        """
        self.window.buttonLoadH1.clicked.connect(
            self.controllerConfig.loadHomographyRgbTodepth)

    def ConnectButtonLoadHomography2(self):
        """
        docstring
        """
        self.window.buttonLoadH2.clicked.connect(
            self.controllerConfig.loadHomographyThermalToRgb)

    def ConnectButtonSaveConfig(self):
        """
        """
        self.window.buttonSaveConfig.clicked.connect(
            self.controllerConfig.saveConfiguration
        )
