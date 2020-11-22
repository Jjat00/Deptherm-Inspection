from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'


class StylesExtrinsicCalibration():
    def __init__(self, widget):
        super(StylesExtrinsicCalibration).__init__()
        self.widgetAcq = widget
        self.setTheme()
        self.setIcons()
        self.formStyle()

    def setTheme(self):
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
        relativePathIcons = 'modules/ExtrinsicCalibration/public/icons/'
        self.widgetAcq.window.loadButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.widgetAcq.window.loadButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.startButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'play.png'))
        self.widgetAcq.window.startButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.saveButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'save.png'))
        self.widgetAcq.window.saveButton.setIconSize(QtCore.QSize(23, 23))

        self.widgetAcq.window.previusButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'previous.png'))
        self.widgetAcq.window.previusButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.nextButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'skip.png'))
        self.widgetAcq.window.nextButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.clearButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'refresh.png'))
        self.widgetAcq.window.clearButton.setIconSize(QtCore.QSize(25, 25))

        self.widgetAcq.window.uploadButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'cloud.png'))
        self.widgetAcq.window.uploadButton.setIconSize(QtCore.QSize(25, 25))

    def formStyle(self):
        styleWindow = """
            QWidget{
                background: """ + self.secondaryColor + """;
                color:  """ + self.primaryText + """;
                border: none;
                font: Ubuntu;
                font-size: 12pt;
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
            margin: 0;
        """
        self.widgetAcq.window.frameWorkspace.setStyleSheet(styleFrameCamera)

        styleFrameParameters = """
            color: """+self.primaryText+""";
            font: Regular;
        """
        self.widgetAcq.window.textBrowser.setStyleSheet(styleFrameCamera)

        navButtons = """
            background: """+self.frameCamera+""";
            min-height: 30px;
            min-width: 30px;
        """
        self.widgetAcq.window.previusButton.setStyleSheet(navButtons)
        self.widgetAcq.window.nextButton.setStyleSheet(navButtons)
