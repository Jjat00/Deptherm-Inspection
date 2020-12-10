from PySide2 import QtGui, QtCore
relativePathIcons = 'modules/IntrinsicCalibration/public/icons/'

class StylesIntrinsicCalibration():
    def __init__(self, widget):
        super(StylesIntrinsicCalibration).__init__()
        self.widgetAcq = widget
        self.setTheme()
        self.setIcons()
        self.formStyle()

    def setTheme(self):
        self.primaryColor = '#f44333'
        self.secondaryColor = '#ffffff'
        self.buttons = '#ffffff'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ff795e'
        self.lineEdit = '#263238'


    def setIcons(self):
        self.widgetAcq.window.loadButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.widgetAcq.window.loadButton.setIconSize(QtCore.QSize(25, 25))
        self.widgetAcq.window.loadButton.setToolTip('Load images')

        self.widgetAcq.window.startButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'play.png'))
        self.widgetAcq.window.startButton.setIconSize(QtCore.QSize(25, 25))
        self.widgetAcq.window.startButton.setToolTip('start intrinsic calibration')

        self.widgetAcq.window.saveButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'save.png'))
        self.widgetAcq.window.saveButton.setIconSize(QtCore.QSize(25, 25))
        self.widgetAcq.window.saveButton.setToolTip('save intrinsic parameters')

        self.widgetAcq.window.previusButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'previous.png'))
        self.widgetAcq.window.previusButton.setIconSize(QtCore.QSize(20, 20))
        self.widgetAcq.window.previusButton.setToolTip('previus')

        self.widgetAcq.window.nextButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'skip.png'))
        self.widgetAcq.window.nextButton.setIconSize(QtCore.QSize(20, 20))
        self.widgetAcq.window.nextButton.setToolTip('next')

        self.widgetAcq.window.clearButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'refresh.png'))
        self.widgetAcq.window.clearButton.setIconSize(QtCore.QSize(25, 25))
        self.widgetAcq.window.clearButton.setToolTip('clear wokspace')

        self.widgetAcq.window.buttonUploadCloud.setIcon(
            QtGui.QPixmap(relativePathIcons+'cloud.png'))
        self.widgetAcq.window.buttonUploadCloud.setIconSize(QtCore.QSize(32, 32))
        self.widgetAcq.window.buttonUploadCloud.setToolTip(
            'upload to database')

    def formStyle(self):
        styleWindow = """
            QWidget{
                background: """ + self.secondaryColor + """;
                color:  """ + self.primaryText + """;
                font: Ubuntu;
                font-size: 12pt;
            }
            QPushButton{
                Background: """ + self.buttons + """;
                color: """ + self.secondaryColor + """;
                min-height: 40px;
                min-width: 40px;   
            }       
            QPushButton:pressed {
                background-color: rgb(224, 0, 0);
            } 
            QPushButton:hover {
                background-color: """+self.primaryColor+""";
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
            background: """+self.secondaryColor+""";
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """+self.frameCamera+""";
            min-width:200px;
            padding-bottom: 0;
        """
        self.widgetAcq.window.labelHeader.setStyleSheet(styleHeader)

        styleFrameCamera = """
            background: """+self.frameCamera+""";
        """
        self.widgetAcq.window.frameWorkspace.setStyleSheet(styleFrameCamera)

        styleFrameParameters = """
            color: """+self.frameCamera+""";
            font: Regular;
        """
        self.widgetAcq.window.frameDistortion.setStyleSheet(styleFrameParameters)
        self.widgetAcq.window.frameFocal.setStyleSheet(styleFrameParameters)

        navButtons = """
            background: """+self.frameCamera+""";
        """
        self.widgetAcq.window.previusButton.setStyleSheet(navButtons)
        self.widgetAcq.window.nextButton.setStyleSheet(navButtons)
