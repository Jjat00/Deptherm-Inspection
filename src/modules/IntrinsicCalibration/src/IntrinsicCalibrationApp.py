"""
File: IntrinsicCalibrationWidget.py
Author: Jaimen Aza <<Jjat userjjar00@gmail.com>>
Date create: 19-august-2020
Last moditication date : 21-august-2020
"""

from PySide2 import QtWidgets
import sys
import os

dirs = ['views', 'controllers', 'models',
        'components/AcquisitionIntrinsicCalibration/src']

for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

from IntrinsicCalibrationWidget import IntrinsicCalibrationWidget
from MainControllerIntrinsicCalibration import MainControllerIntrinsicCalibration

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    intrinsicCalibrationWidget = IntrinsicCalibrationWidget()
    MainControllerIntrinsicCalibration = MainControllerIntrinsicCalibration(
        intrinsicCalibrationWidget)
    app.exec_()
