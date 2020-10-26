from PySide2 import QtGui, QtCore
relativePathIcons = 'modules/IntrinsicAcquisition/public/icons/'

class StylesIntAcqWidget():
    """
    Set style and icons to widget
    """    

    def __init__(self, widget):
        super(StylesIntAcqWidget).__init__()
        self.widgetAcq = widget
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

    def setIcons(self):
        self.widgetAcq.window.onButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'camera.png'))
        self.widgetAcq.window.onButton.setIconSize(QtCore.QSize(30, 30))

        self.widgetAcq.window.offButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'stop.png'))
        self.widgetAcq.window.offButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.captureButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'capture.png'))
        self.widgetAcq.window.captureButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.saveButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'storage.png'))
        self.widgetAcq.window.saveButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.startButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'play.png'))
        self.widgetAcq.window.startButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.stopButton.setIcon(
            QtGui.QPixmap(relativePathIcons + 'stop.png'))
        self.widgetAcq.window.stopButton.setIconSize(QtCore.QSize(20, 20))

    def formStyle(self):
        styleWindow = """
            QWidget{
                    background: """ + self.secondaryColor + """;
                    color:  """ + self.primaryText + """;
                    border: none;
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QTabWidget::tab-bar{
                    alignment: right;
                }
                QTabBar{
                    background: """ + self.primaryColor + """;
                }
                QTabBar::tab {
                    background: """ + self.primaryColor + """;
                    min-width: 10px;
                    margin: 5px;
                    margin-bottom: 10px;
                }
                QTabBar::tab:hover {
                    color: """ + self.secondaryColor + """;
                }            
                QTabBar::tab:selected {
                    background: """ + self.primaryColor + """;
                    Color: """ + self.primaryText + """;
                }
                QTabBar::tab:!selected {
                    Color: """ + self.frameCamera + """;
                }
                QTabBar::tab:!selected:hover {
                    Color: """ + self.primaryText + """;
                }
                QPushButton{
                    Background: """ + self.buttons + """;
                    Background: """ + self.buttons + """;
                    color: """ + self.secondaryColor + """;
                    min-height: 40px;
                    border-radius: 2px;
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                    border-style: inset;
                } 
                QPushButton:hover {
                    background-color: """+self.primaryColor+""";
                    border-style: inset;
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
            """
        self.widgetAcq.setStyleSheet(styleWindow)

        styleHeader = """
            padding-left: 5px;
            background: """ + self.secondaryColor + """;
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """ + self.frameCamera + """;
            min-width:200px;
            padding-bottom: 0;
        """
        self.widgetAcq.window.labelHeader.setStyleSheet(styleHeader)

        styleFrameCamera = """
            background: """ + self.frameCamera + """;
        """
        self.widgetAcq.window.frameCameraM.setStyleSheet(styleFrameCamera)
        self.widgetAcq.window.frameCameraA.setStyleSheet(styleFrameCamera)
        
        styleLabelNoImage = """
            background: """ + self.secondaryColor + """;
            color: """ + self.frameCamera + """;
            font: bold, Ubuntu sans-serif;
            font-size: 14pt;
        """
        self.widgetAcq.window.labelNoImage.setStyleSheet(styleLabelNoImage)
