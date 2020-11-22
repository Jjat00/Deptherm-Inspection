from PySide2 import QtWidgets

from models.interfaces.ClientDB import insertClient
from controllers.ControllerConfigInspec import ControllerConfigInspec
from views.configurationInspection.InspectionConfigurationWidget import InspectionConfigurationWidget

class ControllerClientInspection():
    """
    Controller for inspection configuration 
    """

    def __init__(self, mainWidget, clienWidget):
        super().__init__()
        self.mainWindow = mainWidget.window
        self.mainWidget = mainWidget
        self.window = clienWidget.window
        self.connectButtons()
        clienWidget.exec()
        self.register = False

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonCancel.clicked.connect(
            self.cleanLineEdit)
        self.window.buttonSave.clicked.connect(
            self.registerClient)
        self.window.buttonNext.clicked.connect(
            self.next)

    def next(self):
        self.mainWidget.cleanWorkspace()
        self.widgetConfig = InspectionConfigurationWidget()
        self.mainWindow.layoutDepthermInpesction.addWidget(
            self.widgetConfig)
        ControllerConfigInspec(self.mainWidget, self.widgetConfig)

    def getVulesLineEdit(self):
        """
        get values fron line text form
        """
        try:
            self.showMesagge("")
            self.ID = int(self.window.lineEditID.text())
            self.name = self.window.lineEditName.text()
            self.lastname = self.window.lineEditLastname.text()
            self.company = self.window.lineEditCompany.text()
            self.phone = int(self.window.lineEditPhone.text())
            self.email = self.window.lineEditEmail.text()
            self.register = True
        except ValueError:
            self.showMesagge("incorrect data")
            self.register = False

    def registerClient(self):
        """
        Handler button register user
        """
        try:
            self.getVulesLineEdit()
            if self.ID != None and self.register:
                print(self.ID, self.name, self.lastname,
                            self.company, self.phone, self.email)
                res = insertClient(self.ID, self.name, self.lastname,
                             self.company, self.phone, self.email)
                if res == 200:
                    self.showMesagge("cient registered successfully")
                else:
                    self.showMesagge("cient is already registered")
                #self.cleanLineEdit()
        except AttributeError:
            print("Fail register user")

    def showMesagge(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)

    def cleanLineEdit(self):
        """
        Clear line edit
        """
        self.window.lineEditID.setText("")
        self.window.lineEditName.setText("")
        self.window.lineEditLastname.setText("")
        self.window.lineEditEmail.setText("")
        self.window.lineEditPhone.setText("")
        self.window.lineEditCompany.setText("")
        self.ID = None
