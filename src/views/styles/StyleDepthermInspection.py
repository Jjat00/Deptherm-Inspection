from views.styles.Style import Styles
from PySide2 import QtGui, QtCore
relativePathIcons = '../public/icons/'

class StyleDepthermInspection():
    """
    Deptherm Inspection widget style
    """
    def __init__(self, widget):
        super(StyleDepthermInspection).__init__()
        self.widget = widget
        self.styles = Styles(self.widget)
        self.setIcons()
        self.setStyle()

    def setIcons(self):
        """
        Set icons GUI
        """
        self.widget.window.buttonUserManage.setIcon(
            QtGui.QPixmap(relativePathIcons+'management.png'))
        self.widget.window.buttonUserManage.setIconSize(
            QtCore.QSize(30, 30))
        self.widget.window.buttonUserManage.setToolTip('Management user')

        self.widget.window.buttonLogin.setIcon(
            QtGui.QPixmap(relativePathIcons+'login1.png'))
        self.widget.window.buttonLogin.setIconSize(QtCore.QSize(30, 30))
        self.widget.window.buttonLogin.setToolTip('User login')

        self.widget.window.buttonInspection.setIcon(
            QtGui.QPixmap(relativePathIcons+'add.png'))
        self.widget.window.buttonInspection.setIconSize(
            QtCore.QSize(30, 30))
        self.widget.window.buttonInspection.setToolTip('New inspection')

        self.widget.window.buttonCalibInt.setIcon(
            QtGui.QPixmap(relativePathIcons+'intrinsicCalib.png'))
        self.widget.window.buttonCalibInt.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonCalibInt.setToolTip('Intrinsic calibration')

        self.widget.window.buttonCalibExt.setIcon(
            QtGui.QPixmap(relativePathIcons+'extrinsicCalib.png'))
        self.widget.window.buttonCalibExt.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonCalibExt.setToolTip('Extrinsic calibration')

        self.widget.window.buttonInspectionAnalyzer.setIcon(
            QtGui.QPixmap(relativePathIcons+'3dsensor.png'))
        self.widget.window.buttonInspectionAnalyzer.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonInspectionAnalyzer.setToolTip('Camera Fusion')

        self.widget.window.buttonLogout.setIcon(
            QtGui.QPixmap(relativePathIcons+'logout.png'))
        self.widget.window.buttonLogout.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonLogout.setToolTip('Logout')

        self.widget.window.buttonReport.setIcon(
            QtGui.QPixmap(relativePathIcons+'report.png'))
        self.widget.window.buttonReport.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonReport.setToolTip('Generate report')

        self.widget.window.buttonAcquisition.setIcon(
            QtGui.QPixmap(relativePathIcons+'cmaeravideo.png'))
        self.widget.window.buttonAcquisition.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonAcquisition.setToolTip('Acquisition')

        self.widget.window.buttonClean.setIcon(
            QtGui.QPixmap(relativePathIcons+'clean.png'))
        self.widget.window.buttonClean.setIconSize(
            QtCore.QSize(40, 40))
        self.widget.window.buttonClean.setToolTip('Clean workspace')

        labelLogo = QtGui.QPixmap.fromImage(relativePathIcons+'PSI_LOGO.png')
        self.widget.window.labelLogo.setPixmap(labelLogo)
        self.widget.window.labelLogo.setScaledContents(True)

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

        styleFrameCamera = """
            background: """+self.styles.frameCamera+""";
            margin: 0;
        """
        self.widget.window.frameWorkspace.setStyleSheet(styleFrameCamera)

        styleMessage = """
            padding-left: 5px;
            font-size: 17pt;
            color: """ + self.styles.primaryColor + """;
            padding-bottom: 0;
        """
        self.widget.window.labelMessage.setStyleSheet(styleMessage)

