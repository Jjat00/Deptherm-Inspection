from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'


class Styles():
    def __init__(self, widget):
        super(Styles).__init__()
        self.widget = widget
        self.themeLight()
        self.setFormStyle()

    def themeDark(self):
        self.primaryColor = '#f44333'
        self.secondaryColor = '#263238'
        #self.secondaryColor = 'white'
        self.buttons = '#00E676'
        #self.buttons = 'white'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ff795e'
        self.lineEdit = '#263238'

    def themeLight(self):
        self.primaryColor = '#b90008'
        self.secondaryColor = '#ffffff'
        self.buttons = '#e53935'
        self.frameCamera = '#e0e0e0'
        self.primaryText = '#212121'
        self.secondaryText = '#000a12'
        self.lineEdit = '#f5f5f5'
        self.progressBar = '#ff795e'

    def setFormStyle(self):
        styleWindow = """
            QWidget{
                    background: """+self.secondaryColor+""";
                    color:  """+self.primaryText+""";
                    border: none;
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
                    color: """+self.primaryColor+""";
                }            
                QTabBar::tab:selected {
                    background: """+self.primaryColor+""";
                    Color: """+self.primaryText+""";
                }
                QTabBar::tab:!selected {
                    Color: """+self.secondaryColor+""";
                }
                QTabBar::tab:!selected:hover {
                    Color: """+self.secondaryText+""";
                }
                QPushButton{
                    Background: """+self.buttons + """;
                    Background: """+self.buttons + """;
                    color: """+self.secondaryColor + """;
                    min-height: 40px;
                    min-width: 80px;
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                    border-style: inset;
                } 
                QPushButton:hover {
                    background-color: #B71C1C;
                    border-style: inset;
                } 
                QComboBox{
                    Background: """+self.secondaryColor + """;
                    color: """+self.primaryText + """;
                    min-height: 25px;
                }        
                QComboBox QAbstractItemView {
                    border: 2px solid darkgray;
                    selection-background-color: lightgray;
                }
                QLineEdit { 
                    Background: """+self.lineEdit + """;    
                    color:  """+self.secondaryText+""";
                    border: 1px solid """+self.primaryColor + """;    
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
            """
        self.widget.setStyleSheet(styleWindow)
