class Calibration():
    """ 
    Model for calibration table
    """

    def __init__(self, idCalibration, userID, calibrationType,
                 focalParameters, distortionParameters, matrizHomografia):
        self.idCalibration = idCalibration
        self.userID = userID
        self.calibrationType = calibrationType
        self.focalParameters = focalParameters
        self.distortionParameters = distortionParameters
        self.matrizHomografia = matrizHomografia

    def getIdCalibration(self):
        return self.idCalibration

    def setIdCalibration(self, idCalibration: int):
        self.idCalibration = idCalibration
