from views.styles.Style import Styles
from PySide2 import QtGui

relativePathIcons = '../public/icons/'

class StyleAcquisitionManagement():
    """
    User management widget style
    """

    def __init__(self, widget):
        super(StyleAcquisitionManagement).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        self.setStyle()
        self.setIcons()

    def setIcons(self):
        patron1 = QtGui.QPixmap.fromImage(
            relativePathIcons+'patron.png')
        self.widget.window.labelIntrinsic.setPixmap(patron1)
        self.widget.window.labelIntrinsic.setScaledContents(True)
        patron2 = QtGui.QPixmap.fromImage(
            relativePathIcons+'patron2.png')
        self.widget.window.labelExtrinsic.setPixmap(patron2)
        self.widget.window.labelExtrinsic.setScaledContents(True)
        allCameras = QtGui.QPixmap.fromImage(
            relativePathIcons+'3dsensor.png')
        self.widget.window.labelAllcameras.setPixmap(allCameras)
        self.widget.window.labelAllcameras.setScaledContents(True)


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

