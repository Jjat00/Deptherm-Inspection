from PySide2 import QtWidgets

from MainControllerIntrinsicAcq import MainControllerIntrinsicAcq
from IntrinsicAcquisitionWidget import IntrinsicAcquisitionWidget

from MainControllerExtrinsicAcq import MainControllerExtrinsicAcq
from ExtrinsicAcquisitionWidget import ExtrinsicAcquisitionWidget

class ControllerAcquisition():
    """
    Controller for user management form
    """

    def __init__(self, mainWidget,  managemetWidget):
        super(ControllerAcquisition).__init__()
        self.mainWidget = mainWidget
        self.window = managemetWidget.window
        self.connectButtons()
        managemetWidget.exec()

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        try:
            self.window.buttonIntAcq.clicked.connect(
                self.showIntrinsicAcquisition)
            self.window.buttonExtAcq.clicked.connect(
                self.showExtrinsicAcquisition)
            self.window.buttonAllAcq.clicked.connect(
                self.showAllCamerasAcquisition)
        except:
            pass

    def showIntrinsicAcquisition(self):
        """
        Show intrinsic acquisition widget into main widget
        """
        self.mainWidget.cleanWorkspace()
        intrinsicAcquisitionWidget = IntrinsicAcquisitionWidget()
        self.mainWidget.window.layoutWorkspace.addWidget(intrinsicAcquisitionWidget)
        MainControllerIntrinsicAcq(intrinsicAcquisitionWidget)

    def showExtrinsicAcquisition(self):
        """
        Show extrinsic acquisition widget into main widget
        """
        self.mainWidget.cleanWorkspace()
        extrinsicAcquisitionWidget = ExtrinsicAcquisitionWidget()
        self.mainWidget.window.layoutWorkspace.addWidget(
            extrinsicAcquisitionWidget)
        MainControllerExtrinsicAcq(extrinsicAcquisitionWidget)

    def showAllCamerasAcquisition(self):
        """
        Handler button consult user
        """
        pass
