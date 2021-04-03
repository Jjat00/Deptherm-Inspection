import cv2
import numpy as np

homographyMatrix = np.array([
    [0.982783162563725, -0.1037948203827874, -67.25266758555863],
    [0.10492263205175319, 0.937794282967404, 17.40358087186924],
    [6.980203268892067e-05, -0.00010533616619914174, 1.0]
])


def term2rb(term):
    
    imageDst = cv2.warpPerspective(term,
                                   homographyMatrix, term.shape[::-1][1:3])
    return imageDst


relativePathRgb = '../modules/AcquisitionExtrinsicCalibration/data/images/ollThermal.png'

image = cv2.imread(relativePathRgb)
rimage = cv2.imread(
    '../modules/AcquisitionExtrinsicCalibration/data/images/ollRgb.png')
newImage = term2rb(image)

cv2.imshow('original', image)
cv2.imshow('newImage', newImage)
cv2.imshow('fusion', newImage+rimage)
cv2.waitKey(0)
key = cv2.waitKey(1)
if key == ord('q'):
    cv2.destroyAllWindows()
