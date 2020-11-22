from PySide2 import QtWidgets

from models.interfaces.ConfigurationDB import insertConfig

class ControllerConfigInspec():
    """
    Controller for inspection configuration 
    """

    def __init__(self, mainWidget, configWidget):
        super().__init__()
        self.mainWidget = mainWidget
        self.mainWindow = mainWidget.window
        self.window = configWidget.window
        self.connectButtons()
        configWidget.exec()
        self.register = False

    def connectButtons(self):
        """
        Connect the buttons with their events
        """
        self.window.buttonCancel.clicked.connect(
            self.cleanLineEdit)
        self.window.buttonSave.clicked.connect(
            self.registerConfig)
        self.window.pushButtonFinish.clicked.connect(
            self.getVulesLineEdit)

    def getVulesLineEdit(self):
        """
        get values fron line text form
        """
        try:
            self.showMesagge("")
            self.name = self.window.lineEditName.text()
            self.place = self.window.lineEditPlace.text()
            self.emissivity = float(self.window.lineEditEmissivity.text())
            self.temp = float(self.window.lineEditTemp.text())
            self.order = self.window.textEditOrder.toPlainText()
            self.register = True
        except ValueError:
            self.showMesagge("incorrect data")
            self.register = False

    def registerConfig(self):
        self.getVulesLineEdit()
        if self.register:
            print(self.name, self.place, self.emissivity,
                  self.temp, self.order)
            res = insertConfig(self.name, self.place, self.emissivity,
                         self.temp, self.order)
            if res == 200:
                self.showMesagge("config registered successfully")
            else:
                self.showMesagge("config is already registered")


    def showMesagge(self, message):
        """
        Show response request
        """
        self.window.labelMessage.setText(message)

    def cleanLineEdit(self):
        """
        Clear line edit
        """
        self.window.lineEditName.setText("")
        self.window.lineEditPlace.setText("")
        self.window.lineEditEmissivity.setText("")
        self.window.lineEditTemp.setText("")
        self.window.textEditOrder.setText("")
