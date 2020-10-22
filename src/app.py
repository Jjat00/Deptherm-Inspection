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
Add intrinsic acquisition modules to path
"""
dirs = ['views', 
        'controllers',
        'acquisition']
for nameDir in dirs:
    #intrinsic acquisition
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/AcquisitionIntrinsicCalibration/src/', nameDir))
    sys.path.append(path)
    #extrinsic acquisition
    path = os.path.join(sys.path[0], "%s%s" % (
        'modules/AcquisitionExtrinsicCalibration/src/', nameDir))
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
