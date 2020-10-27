"""
File: ExtrinsicCalibrationWidget.py
Author: Jaimen Aza 
Email: userjjar00@gmail.com
Date create: 21-august-2020
"""
from PySide2 import QtWidgets
import sys
import os


""" 
Add directories to path
"""
dirs = ['views', 'controllers', 'resources',
        'components/AcquisitionExtrinsicCalibration/src/']

for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)


from ExtrinsicCalibrationWidget import ExtrinsicCalibrationWidget
from MainControllerExtCalibration import MainControllerExtCalibration

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = ExtrinsicCalibrationWidget()
    mainControllerExtCalibration = MainControllerExtCalibration(
        acquisitionExtrinsicCalibration)
    app.exec_()
