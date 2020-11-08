from views.styles.Style import Styles
from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'

class StyleUserManagement():
    """
    User management widget style
    """

    def __init__(self, widget):
        super(StyleUserManagement).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        self.setStyle()

    def setStyle(self):
        """
        Set stylesheet componenets GUI
        """

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

        styleMessage = """
            padding-left: 5px;
            font-size: 15pt;
            color: """ + self.styles.primaryColor + """;
            padding-bottom: 0;
        """
        self.widget.window.labelMessage.setStyleSheet(styleMessage)

        styleButtons = """ 
            border: 1px solid """ + self.styles.secondaryText + """;
        """
        self.widget.window.buttonRegisterUser.setStyleSheet(styleButtons)
        self.widget.window.buttonUpdateUser.setStyleSheet(styleButtons)
        self.widget.window.buttonConsultUser.setStyleSheet(styleButtons)
        self.widget.window.buttonDeleteUser.setStyleSheet(styleButtons)
        
