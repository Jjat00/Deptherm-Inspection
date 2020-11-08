from views.styles.Style import Styles
from PySide2 import QtGui, QtCore

class StyleAcquisitionManagement():
    """
    User management widget style
    """

    def __init__(self, widget):
        super(StyleAcquisitionManagement).__init__()
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

        styleButtons = """ 
            border: 1px solid """ + self.styles.secondaryText + """;
        """
        self.widget.window.buttonIntAcq.setStyleSheet(styleButtons)
        self.widget.window.buttonExtAcq.setStyleSheet(styleButtons)
        self.widget.window.buttonAllAcq.setStyleSheet(styleButtons)

