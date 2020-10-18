from views.styles.Style import Styles
from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'

class StyleUserRegister():
    """
    docstring
    """
    def __init__(self, widget):
        super(StyleUserRegister).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        self.setStyle()

    def setStyle(self):
        """
        docstring
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
