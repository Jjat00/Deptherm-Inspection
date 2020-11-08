import cv2.cv2 as cv2
from matplotlib import pyplot as plt
import numpy as np


class FilterImage:
    def __init__(self):
        pass

    def histograma(self, frame):
        bgrColor = ('b', 'g', 'r')
        for i, col in enumerate(bgrColor):
            histr = cv2.calcHist([frame], [i], None, [255], [0, 255])
            plt.plot(histr, color=col)
            plt.xlim([0, 255])
        plt.show()

    def changeColorRange(self, frame, pos, inf, sup, color):
        for i in range(0, len(frame)):
            for j in range(0, len(frame[i])):
                if(frame[i][j][pos] < inf or frame[i][j][pos] > sup):
                    #pos = blue 0, rojo 1, verde 2
                    frame[i][j][pos] = color

        return frame

    def red(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        newFrame = [[[0, 255 % j, j] for j in i] for i in frame_gray]
        dt = np.dtype('f8')
        newFrame = np.array(newFrame, dtype=dt)
        return newFrame

    def blue(self, frame):
        frame[:, :, 0] = 150
        #frame[:,:,1]  = 50
        #frame[:,:,2] = 0
        return frame

    def hsv(self, frame):
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frameHSV[0:240, :, 0] = 30
        frameHSV[240:, :, 0] = 0
        frameHSV[:, :, 1] = 200
        #frameHSV[:,:,2] = 100
        frame = cv2.cvtColor(frameHSV, cv2.COLOR_HSV2BGR)
        #frame[:,:,0] = 100
        return frame

    def bitwise(self, frame):
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowerColor = np.array([0, 40, 30])
        upperColor = np.array([30, 255, 255])
        mask = cv2.inRange(hsvFrame, lowerColor, upperColor)
        #filtro = self.filtro3(frame)
        newFrame = cv2.bitwise_and(frame, frame, mask=mask)
        #newFrame = cv2.bitwise_and(newFrame,filtro)
        newFrame = 50 - newFrame
        #newFrame = newFrame+ frame
        return newFrame

    def log(self, frame):
        c = 200/np.log(256)
        newFrame = c*np.log(1+frame.astype(np.float))
        newFrame = np.array(newFrame, dtype=np.uint8)
        #newFrame = newFrame+ frame
        return newFrame

    def power(self, frame):
        r = 0.9
        c = 255/np.power(255, r)
        newFrame = c*np.power(1+frame.astype(np.float), r)
        newFrame = np.array(newFrame, dtype=np.uint8)
        #newFrame = newFrame-frame
        return newFrame