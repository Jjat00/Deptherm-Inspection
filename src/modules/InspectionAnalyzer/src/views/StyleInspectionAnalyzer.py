from PySide2 import QtCore, QtGui
from PySide2 import *

relativePathIcons = 'modules/InspectionAnalyzer/public/icons/'


class StyleInspectionAnalyzer():
    def __init__(self, widget):
        super(StyleInspectionAnalyzer).__init__()
        self.cameraFusionWidget = widget
        self.themeHighContrast()
        self.setIcons()
        self.formStyle()

    def themeHighContrast(self):
        """ 
        set color high constrast 
        """
        self.primaryColor = '#f44333'
        self.secondaryColor = '#ffffff'
        self.buttons = '#ffffff'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ff795e'
        self.lineEdit = '#263238'

    def theme1(self):
        self.primaryColor = '#f44333'
        self.secondaryColor = '#263238'
        self.buttons = '#00E676'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ee98fb'
        self.lineEdit = '#263238'

    def setIcons(self):
        self.cameraFusionWidget.window.buttonTurnOn.setIcon(
            QtGui.QPixmap(relativePathIcons+'video.png'))
        self.cameraFusionWidget.window.buttonTurnOn.setIconSize(
            QtCore.QSize(20, 20))

        self.cameraFusionWidget.window.buttonTurnOn.setToolTip('turn on cameras')

        self.cameraFusionWidget.window.buttonCapture.setIcon(
            QtGui.QPixmap(relativePathIcons+'capture.png'))
        self.cameraFusionWidget.window.buttonCapture.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonCapture.setToolTip(
            'capture images')

        """ self.cameraFusionWidget.window.buttonSaveImages.setIcon(
            QtGui.QPixmap(relativePathIcons+'storage.png'))
        self.cameraFusionWidget.window.buttonSaveImages.setIconSize(
            QtCore.QSize(20, 20)) """

        self.cameraFusionWidget.window.buttonShowPointCamera.setIcon(
            QtGui.QPixmap(relativePathIcons+'ojo.png'))
        self.cameraFusionWidget.window.buttonShowPointCamera.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonShowPointCamera.setToolTip(
            'show point cloud')

        self.cameraFusionWidget.window.buttonSavePointCloud.setIcon(
            QtGui.QPixmap(relativePathIcons+'storage.png'))
        self.cameraFusionWidget.window.buttonSavePointCloud.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonSavePointCloud.setToolTip(
            'save data')

        self.cameraFusionWidget.window.buttonClean.setIcon(
            QtGui.QPixmap(relativePathIcons+'escoba.png'))
        self.cameraFusionWidget.window.buttonClean.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonClean.setToolTip(
            'clean workspace')

        #################################################################
        self.cameraFusionWidget.window.buttonLoadDepth.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadDepth.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonLoadRgb.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadRgb.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonLoadThermal.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadThermal.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonShowPointImages.setIcon(
            QtGui.QPixmap(relativePathIcons+'ojo.png'))
        self.cameraFusionWidget.window.buttonShowPointImages.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonSavePointCloudI.setIcon(
            QtGui.QPixmap(relativePathIcons+'storage.png'))
        self.cameraFusionWidget.window.buttonSavePointCloudI.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonClearI.setIcon(
            QtGui.QPixmap(relativePathIcons+'escoba.png'))
        self.cameraFusionWidget.window.buttonClearI.setIconSize(
            QtCore.QSize(20, 20))

        #################################
        self.cameraFusionWidget.window.showDepth.setIcon(
            QtGui.QPixmap(relativePathIcons+'3d.png'))
        self.cameraFusionWidget.window.showDepth.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.showDepth.setToolTip(
            'depth image')

        self.cameraFusionWidget.window.showRGB.setIcon(
            QtGui.QPixmap(relativePathIcons+'rgb.png'))
        self.cameraFusionWidget.window.showRGB.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.showRGB.setToolTip(
            'rgb image')

        self.cameraFusionWidget.window.showThermal.setIcon(
            QtGui.QPixmap(relativePathIcons+'thermometer.png'))
        self.cameraFusionWidget.window.showThermal.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.showThermal.setToolTip(
            'thermal image')

        self.cameraFusionWidget.window.showThermalRgb.setIcon(
            QtGui.QPixmap(relativePathIcons+'thermometerRGB.png'))
        self.cameraFusionWidget.window.showThermalRgb.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.showThermalRgb.setToolTip(
            'rgb-thermal')

        self.cameraFusionWidget.window.showRgbDepth.setIcon(
            QtGui.QPixmap(relativePathIcons+'3dRGB.png'))
        self.cameraFusionWidget.window.showRgbDepth.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.showRgbDepth.setToolTip(
            'rgb-depth')

        self.cameraFusionWidget.window.buttonHistogram.setIcon(
            QtGui.QPixmap(relativePathIcons+'histogram.png'))
        self.cameraFusionWidget.window.buttonHistogram.setIconSize(
            QtCore.QSize(30, 30))
        self.cameraFusionWidget.window.buttonHistogram.setToolTip(
            'histogram')

        self.cameraFusionWidget.window.buttonStartICP.setIcon(
            QtGui.QPixmap(relativePathIcons+'play.png'))
        self.cameraFusionWidget.window.buttonStartICP.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonStartICP.setToolTip(
            'start icp')

        self.cameraFusionWidget.window.buttonShowPointRegister.setIcon(
            QtGui.QPixmap(relativePathIcons+'ojo.png'))
        self.cameraFusionWidget.window.buttonShowPointRegister.setIconSize(
            QtCore.QSize(20, 20))
        self.cameraFusionWidget.window.buttonShowPointRegister.setToolTip(
            'show point cloud register')

        ##############################################
        self.cameraFusionWidget.window.buttonLoadIntrinsic.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadIntrinsic.setIconSize(
            QtCore.QSize(25, 25))
        self.cameraFusionWidget.window.buttonLoadIntrinsic.setToolTip(
            'load intrinsic matrix')

        self.cameraFusionWidget.window.buttonLoadH1.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadH1.setIconSize(
            QtCore.QSize(25, 25))
        self.cameraFusionWidget.window.buttonLoadH1.setToolTip(
            'load homography matrix 1')

        self.cameraFusionWidget.window.buttonLoadH2.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.cameraFusionWidget.window.buttonLoadH2.setIconSize(
            QtCore.QSize(25, 25))
        self.cameraFusionWidget.window.buttonLoadH2.setToolTip(
            'load homography matrix 2')

        self.cameraFusionWidget.window.buttonUpload.setIcon(
            QtGui.QPixmap(relativePathIcons+'cloud.png'))
        self.cameraFusionWidget.window.buttonUpload.setIconSize(
            QtCore.QSize(25, 25))
        self.cameraFusionWidget.window.buttonUpload.setToolTip(
            'upload data to database')

    def formStyle(self):
        styleWindow = """
            QWidget{
                    background: """+self.secondaryColor+""";
                    color:  """+self.primaryText+""";
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QTabWidget::tab-bar{
                    alignment: right;
                }
                QTabBar{
                    background: """+self.primaryColor+""";
                }
                QTabBar::tab {
                    background: """+self.primaryColor+""";
                    min-width: 10px;
                    margin: 5px;
                    margin-bottom: 10px;
                }
                QTabBar::tab:hover {
                    color: """+self.secondaryColor+""";
                }            
                QTabBar::tab:selected {
                    background: """+self.primaryColor+""";
                    Color: """+self.secondaryColor+""";
                }
                QTabBar::tab:!selected {
                    Color: """+self.primaryText+""";
                }
                QTabBar::tab:!selected:hover {
                    Color: """+self.secondaryColor+""";
                }
                QPushButton{
                    Background: """+self.buttons + """;
                    color: """+self.secondaryColor + """;
                    min-height: 40px;
                    min-width: 40px;                   
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                } 
                QPushButton:hover {
                    background-color: #B71C1C;
                } 
                QComboBox {
                    Background: """ + self.primaryText + """;
                    color: """ + self.lineEdit + """;
                    min-height: 25px;
                }   
                QComboBox:!selected {
                    Background: """ + self.primaryText + """;
                    color: """ + self.lineEdit + """;
                }   
                QComboBox:!on {
                    Background: """ + self.primaryText + """;
                    color: """ + self.lineEdit + """;
                } 
                QLineEdit { 
                    Background: """ + self.primaryText + """;    
                    color:  """ + self.lineEdit + """;
                    border: 1px solid """ + self.secondaryText + """;    
                    text-align: center;
                } 
                QLabel {
                    color: """+self.secondaryText + """;
                    font-size: 11pt;
                    font: bold;
                }
                QProgressBar {
                    color: """+self.secondaryText + """;
                    background: """+self.secondaryColor+""";
                    border: none;
                }
                QProgressBar::chunk {
                    color: """+self.progressBar+""";
                    background: """+self.progressBar+""";
                    border: none;
                }     
                QCheckBox {
                    color: """+self.secondaryText + """;
                    font-size: 11pt;
                    font: bold;
                }     
                QTextBrowser { 
                    Background: """ + self.primaryText + """;    
                    color:  """ + self.lineEdit + """;
                    border: 1px solid """ + self.secondaryText + """;    
                    text-align: center;
                    font-size: 11pt;
                }                       
            """
        self.cameraFusionWidget.setStyleSheet(styleWindow)

        styleHeader = """
            padding-left: 5px;
            background: """+self.buttons+""";
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """+self.frameCamera+""";
            min-width:200px;
            padding-bottom: 0;
        """
        self.cameraFusionWidget.window.labelHeader.setStyleSheet(styleHeader)
        self.cameraFusionWidget.window.labelHeaderSetting.setStyleSheet(
            styleHeader)

        styleFrameCamera = """
            background: """+self.frameCamera+""";
            margin: 0;
        """
        self.cameraFusionWidget.window.frameCameras.setStyleSheet(styleFrameCamera)
        self.cameraFusionWidget.window.framePointCloud.setStyleSheet(styleFrameCamera)
        self.cameraFusionWidget.window.frameImages.setStyleSheet(styleFrameCamera)
        self.cameraFusionWidget.window.framePCloudM.setStyleSheet(
            styleFrameCamera)
