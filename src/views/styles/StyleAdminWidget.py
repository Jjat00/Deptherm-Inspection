from views.styles.Style import Styles
from PySide2 import QtGui, QtCore

relativePathIcons = '../public/icons/'


class StyleAdminWidget():
    def __init__(self, widget):
        super(StyleAdminWidget).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        self.setStyle()
        self.setIcons()

    def setIcons(self):
        self.widget.window.buttonLogout.setIcon(
            QtGui.QPixmap(relativePathIcons+'logout.png'))
        self.widget.window.buttonLogout.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonLogout.setToolTip('Logout')

    def setStyle(self):
        styleWindow = """
            QWidget{
                    background: """+self.styles.secondaryColor+""";
                    color:  """+self.styles.primaryText+""";
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QTabWidget::tab-bar{
                    alignment: right;
                }
                QTabBar{
                    background: """+self.styles.primaryColor+""";
                }
                QTabBar::tab {
                    background: """+self.styles.primaryColor+""";
                    min-width: 10px;
                    margin: 5px;
                    margin-bottom: 10px;
                }
                QTabBar::tab:hover {
                    color: """+self.styles.secondaryColor+""";
                }            
                QTabBar::tab:selected {
                    background: """+self.styles.primaryColor+""";
                    Color: """+self.styles.secondaryColor+""";
                }
                QTabBar::tab:!selected {
                    Color: """+self.styles.primaryText+""";
                }
                QTabBar::tab:!selected:hover {
                    Color: """+self.styles.secondaryColor+""";
                }
                QPushButton{
                    Background: """+self.styles.buttons + """;
                    color: """+self.styles.secondaryColor + """;
                    min-height: 40px;
                    min-width: 40px;                   
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                } 
                QPushButton:hover {
                    background-color: #B71C1C;
                } 
                QLabel {
                    color: """+self.styles.secondaryText + """;
                    font-size: 11pt;
                    font: bold;
                }                        
            """
        self.widget.window.setStyleSheet(styleWindow)

        styleHeader = """
            padding-left: 5px;
            background: """ + self.styles.primaryColor + """;
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """ + self.styles.secondaryColor + """;
            min-width:200px;
            padding-bottom: 0;
        """
        self.widget.window.labelHeader.setStyleSheet(styleHeader)

        styleButtonReport = """
            color: """+self.styles.primaryColor+""";
            border: 1px solid """ + self.styles.secondaryText + """;
        """
        self.widget.window.buttonReports.setStyleSheet(
            styleButtonReport)
        self.widget.window.buttonManUser.setStyleSheet(
            styleButtonReport)
        #self.widget.window.buttonAddReport.setStyleSheet(
        #    styleButtonReport)
