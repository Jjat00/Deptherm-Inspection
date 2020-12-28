from HandlerButtonsCamerasTab import HandlerButtonsCamerasTab
from HandlerButtonsImagesTab import HandlerButtonsImagesTab

from configurationInspection.ClientFormWidget import ClientFormWidget
from ControllerClient import ControllerClientInspection

from configurationInspection.InspectionConfigurationWidget import InspectionConfigurationWidget
from ControllerConfigInspec import ControllerConfigInspec

class MainControllerInspection():
    """
    docstring
    """
    def __init__(self, inspectionAnalyzerWidget):
        print('init MainControllerInspection')
        self.window = inspectionAnalyzerWidget.window

        self.HandlerCamerasTab = HandlerButtonsCamerasTab(self.window)
        self.HandlerImagesTab = HandlerButtonsImagesTab(self.window)

        self.connectButtons()
        self.HandlerCamerasTab.disabledButtuns()
        inspectionAnalyzerWidget.exec()

    def connectButtons(self):
        self.connectButtonsCameraInspectionTab()
        self.window.boxChosenCloudCamera.currentIndexChanged.connect(
            self.connectButtonsCameraInspectionTab)
        self.connectButtonsImagesInspectionTab()
        self.window.boxChosenCloudImages.currentIndexChanged.connect(
            self.connectButtonsImagesInspectionTab)

        self.connectButtonCameraTab()
        self.connectButtonAddClient()
        self.connectButtonAddConfig()

    def connectButtonCameraTab(self):
        self.HandlerCamerasTab.connectOnButton()
        self.HandlerCamerasTab.connectCaptureButton()
        self.HandlerCamerasTab.connectbuttonSaveData()
        self.HandlerCamerasTab.connectCleanButton()

        self.HandlerCamerasTab.connectShowRGBButton()
        self.HandlerCamerasTab.connectShowDepthButton()
        self.HandlerCamerasTab.connectShowThermalButton()
        self.HandlerCamerasTab.connectShowRgbDepthButton()
        self.HandlerCamerasTab.connectShowThermalRgbButton()
        self.HandlerCamerasTab.connectShowHistogramButton()

        self.HandlerCamerasTab.connectShowRegisterCloud()
        self.HandlerCamerasTab.connectStartICPButton()

        self.HandlerCamerasTab.connectUploadData()

        self.HandlerCamerasTab.ConnectButtonLoadIntrinsic()
        self.HandlerCamerasTab.ConnectButtonLoadHomography1()
        self.HandlerCamerasTab.ConnectButtonLoadHomography2()

    def connectButtonAddClient(self):
        self.window.buttonAddClient.clicked.connect(
            self.showFormClient)

    def connectButtonAddConfig(self):
        self.window.buttonAddConfig.clicked.connect(
            self.showFormConfig)

    def showFormClient(self):
        self.clientFormWidgetWidget = ClientFormWidget()
        ControllerClientInspection(self.clientFormWidgetWidget)

    def showFormConfig(self):
        self.inspectionConfigurationWidget = InspectionConfigurationWidget()
        ControllerConfigInspec(self.inspectionConfigurationWidget)

    def connectButtonsCameraInspectionTab(self):
        chosenCamera = self.window.boxChosenCloudCamera.currentText()
        if chosenCamera == 'point cloud':
            print('point cloud camera')
            self.HandlerCamerasTab.connectButtonPointCloud()
        if chosenCamera == 'color point cloud':
            print('color point cloud camera')
            self.HandlerCamerasTab.connectButtonColorPointCloud()

    def connectButtonsImagesInspectionTab(self):
        chosenCamera = self.window.boxChosenCloudImages.currentText()
        self.HandlerImagesTab.connectButtonLoadRgbImage()
        self.HandlerImagesTab.connectButtonLoadDepthImage()
        self.HandlerImagesTab.connectButtonLoadThremalImage()
        if chosenCamera == 'point cloud':
            self.HandlerImagesTab.connectButtonDepthToCloud()
        if chosenCamera == 'rgb point cloud':
            self.HandlerImagesTab.connectButtonDepthToColorCloud()
        if chosenCamera == 'thermal point cloud':
            self.HandlerImagesTab.connectButtonDepthToThermalCloud()
        if chosenCamera == 'rgb-thermal point cloud':
            self.HandlerImagesTab.connectButtonDepthToRgbThermalCloud()
