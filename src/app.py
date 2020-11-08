"""
3D thermographic inspection application

Author: Jaimen Aza 
Email: userjjar00@gmail.com
Date create: 17-Oct-2020
"""

from PySide2 import QtWidgets
import sys
import os


"""
Add directories to path
"""
dirs = ['views', 
        'views/styles/', 
        'controllers', 
        'models', 
        'database', 
        'models/entities/', 
        'models/interfaces/']

for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

""" 
Add acquisition modules to path
"""
dirs = ['views', 
        'controllers',
        'acquisition']
for nameDir in dirs:
    #intrinsic acquisition
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/IntrinsicAcquisition/src/', nameDir))
    sys.path.append(path)
    #extrinsic acquisition
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/AcquisitionExtrinsicCalibration/src/', nameDir))
    sys.path.append(path)
    #acquisition all cameras
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/AcquisitionAllCameras/src/', nameDir))
    sys.path.append(path)

""" 
Add calibration modules to path
"""
dirs = ['views',
        'controllers', 
        'resources']
for nameDir in dirs:
    #intrinsic calibration
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/IntrinsicCalibration/src/', nameDir))
    sys.path.append(path)
    #extrinsic calibration
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/ExtrinsicCalibration/src/', nameDir))
    sys.path.append(path)


""" 
Add inspection analyzer to path
"""
dirs = ['views',
        'controllers',
        'controllers/services',
        'controllers/interfaces']
for nameDir in dirs:
    #intrinsic calibration
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/InspectionAnalyzer/src/', nameDir))
    sys.path.append(path)


"""
Add controller to main widget DepthermInspectionWidget and run QApplication
"""
from controllers.MainControllerDepthermInspection import MainControllerDepthermInspection
from views.DepthermInspectionWidget import DepthermInspectionWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    depthermIspectionWidget = DepthermInspectionWidget()
    mainControllerDepthermInspection = MainControllerDepthermInspection(depthermIspectionWidget)
    app.exec_()
