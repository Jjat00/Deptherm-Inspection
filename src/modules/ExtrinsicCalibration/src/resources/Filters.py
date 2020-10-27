import numpy as np
import cv2


class FilterImage():
    def __init_(self):
        super(FilterImage).__init__()

    def filterRed(self, frame):
        frame[:, :, 0] = 150
        return frame

    def filterLog(self, frame):
        c = 255/np.log(256)
        newFrame = c*np.log(1+frame.astype(np.float))
        newFrame = np.array(newFrame, dtype=np.uint8)
        return newFrame

    def bilateralFilter(self, image):
        blur = cv2.bilateralFilter(image, 15, 75, 75)
        return blur
