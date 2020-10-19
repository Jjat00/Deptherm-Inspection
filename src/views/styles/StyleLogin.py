from views.styles.Style import Styles
from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'


class StyleLogin():
    """
    docstring
    """
    def __init__(self, widget):
        super(StyleLogin).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        #self.setIcons()
        self.setStyle()


    def setIcons(self):
        self.widget.window.acqButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'video.png'))
        self.widget.window.acqButton.setIconSize(QtCore.QSize(20, 20))

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

        styleMessage = """
            padding-left: 5px;
            font-size: 15pt;
            color: """ + self.styles.primaryColor + """;
            padding-bottom: 0;
        """
        self.widget.window.labelMessage.setStyleSheet(styleMessage)
