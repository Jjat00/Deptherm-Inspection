from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'


class Styles():
    """ 
    Main style app
    """

    def __init__(self, widget):
        super(Styles).__init__()
        self.widget = widget
        self.themeHighContrast()
        self.setFormStyle()

    def themeDark(self):
        """ 
        set dark colors
        """
        self.primaryColor = '#f44333'
        self.secondaryColor = '#263238'
        self.buttons = '#00E676'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ff795e'
        self.lineEdit = '#757575'

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

    def themeLight(self):
        """
        set light colors
        """
        self.primaryColor = '#b90008'
        self.secondaryColor = '#ffffff'
        self.buttons = '#e53935'
        self.frameCamera = '#e0e0e0'
        self.primaryText = '#212121'
        self.secondaryText = '#000a12'
        self.lineEdit = '#f5f5f5'
        self.progressBar = '#ff795e'

    def setFormStyle(self):
        """ 
        Set stylesheet componenets GUI
        """
        styleWindow = """
            QWidget {
                    background: """+self.secondaryColor+""";
                    color:  """+self.primaryText+""";
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QPushButton {
                    Background: """+self.buttons + """;
                    color: """+self.frameCamera + """;
                    min-height: 40px;
                    min-width: 80px;
                    border-radius: 0;
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                    border-style: inset;
                } 
                QPushButton:hover {
                    background-color: #B71C1C;
                    border-style: inset;
                }     
                QLabel {
                    color: """ + self.secondaryText + """;
                    font-size: 11pt;
                    font: bold;
                }          
                QLineEdit { 
                    Background: """ + self.primaryText + """;    
                    color:  """ + self.lineEdit + """;
                    border: 1px solid """+ self.secondaryText + """;    
                    text-align: center;
                }           
                QComboBox {
                    Background: """+ self.primaryText + """;
                    color: """ + self.lineEdit + """;
                    min-height: 25px;
                }   
                QComboBox:!selected {
                    Background: """+ self.primaryText + """;
                    color: """ + self.lineEdit + """;
                }   
                QComboBox:!on {
                    Background: """+ self.primaryText + """;
                    color: """ + self.lineEdit + """;
                }   
                QTextBrowser {
                    color: """ + self.lineEdit + """
                }
                QTextEdit {
                    color: """ + self.lineEdit + """
                }
                QTableWidget {
                    color: """ + self.frameCamera + """;
                }
                QHeaderView::section {
                    background-color: #646464;
                    padding: 4px;
                    font-size: 14pt;
                    border-style: none;
                    border-bottom: 1px solid #fffff8;
                    border-right: 1px solid #fffff8;
                }

                QHeaderView::section:horizontal
                {
                    border-top: 1px solid #fffff8;
                }

                QHeaderView::section:vertical
                {
                    border-left: 1px solid #fffff8;
                }         
                QToolTip { 
                    background-color: black; 
                    color: white; 
                    border: black solid 1px
                    }                       
            """
        self.widget.setStyleSheet(styleWindow)
