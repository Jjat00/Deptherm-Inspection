import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import os
import threading
from Filters import FilterImage

class ExtrinsicCameraCalibration():
    def __init__(self, window):
        super(ExtrinsicCameraCalibration).__init__()
        self.window = window
        self.criteria = (cv2.TERM_CRITERIA_EPS +
                         cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.drawChessBoardImagesSource = []
        self.drawChessBoardImagesTarget = []
        self.countNoImageAutoAcq = 0
        self.filters = FilterImage()
        np.set_printoptions(suppress=True)

    def setConfig(self, patternDimensions, whichCamera):
        self.patternDimensions = patternDimensions
        #ideal point real world
        self.objp = np.zeros(
            (self.patternDimensions[0]*self.patternDimensions[1], 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:self.patternDimensions[1],
                                    0:self.patternDimensions[0]].T.reshape(-1, 2)
        #choosen camera                                    
        if whichCamera == 'RGB->DEPTH':
            self.whichCamera = 0
        if whichCamera == 'THERMAL->RGB':
            self.whichCamera = 1
        print(self.whichCamera)

    def startExtrinsicCalibration(self, imagesSrc, imagesDst):
        self.NoImages = len(imagesSrc)
        self.pointsSrc = [[[0, 0]]]
        self.pointsDst = [[[0, 0]]]
        self.auxPointsSrc = [[[0, 0]]]
        self.auxPointsDst = [[[0, 0]]]
        self.imagesSrc = []
        self.imagesDst = []
        for which in range(len(imagesDst)):
            self.imageSrc = cv2.imread(imagesSrc[which])
            
            self.imageDst = cv2.imread(imagesDst[which])
            
            self.filterImagesSrc()
            self.filterImagesDst()
            self.findCorners()
            if (self.retImageSrc and self.retImageDst):
                #images calibration
                self.imagesSrc.append(self.imageSrc.copy())
                self.imagesDst.append(self.imageDst.copy())
                #
                threading.Thread(target=self.increaseProgressBar).start()
                self.subPixelCorners()
                imageDraw1, imageDraw2 = self.drawPatternBoardImages()
                cv2.imshow('img', imageDraw1)
                cv2.waitKey(20)
                cv2.imshow('img', imageDraw2)
                cv2.waitKey(20)
        cv2.destroyAllWindows()

        self.homographyMatrix, _ = cv2.findHomography(
            self.pointsSrc[:len(self.pointsSrc)-1], self.pointsDst[:len(self.pointsDst)-1], cv2.RANSAC, 5.0)
        print("homographyMatrix")
        print(self.homographyMatrix)

    def findCorners(self):
        self.toGray()
        self.findChessCorners()

    def toGray(self):
        self.grayImageSrc = cv2.cvtColor(
            self.imageSrc, cv2.COLOR_BGR2GRAY)
        self.grayImageDst = cv2.cvtColor(
            self.imageDst, cv2.COLOR_BGR2GRAY)

    def findChessCorners(self):
        self.retImageSrc, self.cornersImageSrc = cv2.findChessboardCorners(
            self.grayImageSrc, (self.patternDimensions[1], self.patternDimensions[0]), None)
        self.retImageDst, self.cornersImageDst = cv2.findChessboardCorners(
            self.grayImageDst, (self.patternDimensions[1], self.patternDimensions[0]), None)

    def subPixelCorners(self):
        self.corners2ImageSrc = cv2.cornerSubPix(
            self.grayImageSrc, self.cornersImageSrc, (11, 11), (-1, -1), self.criteria)
        self.pointsSrc = np.vstack(
            (self.corners2ImageSrc.tolist(), self.auxPointsSrc))
        self.auxPointsSrc = self.pointsSrc
        
        self.corners2ImageDst = cv2.cornerSubPix(
            self.grayImageDst, self.cornersImageDst, (11, 11), (-1, -1), self.criteria)
        self.pointsDst = np.vstack(
            (self.corners2ImageDst.tolist(), self.auxPointsDst))
        self.auxPointsDst = self.pointsDst

    def drawPatternBoardImages(self):
        self.grayImageSrc = cv2.cvtColor(
            self.grayImageSrc, cv2.COLOR_GRAY2BGR)
        imageDraw1 = cv2.drawChessboardCorners(
            self.grayImageSrc, (self.patternDimensions[1], self.patternDimensions[0]), 
            self.corners2ImageSrc, self.retImageSrc)
        self.drawChessBoardImagesSource.append(imageDraw1)
        self.grayImageDst = cv2.cvtColor(
            self.grayImageDst, cv2.COLOR_GRAY2BGR)
        imageDraw2 = cv2.drawChessboardCorners(
            self.grayImageDst, (self.patternDimensions[1], self.patternDimensions[0]), 
            self.corners2ImageDst, self.retImageDst)
        self.drawChessBoardImagesTarget.append(imageDraw2)
        return imageDraw1, imageDraw2

    def filterImagesSrc(self):
        self.imageSrc = cv2.resize(
            self.imageSrc, (640, 480), interpolation=cv2.INTER_AREA)
        if self.whichCamera == 1:
            #self.imageSrc = self.filters.filterRed(self.imageSrc)
            #self.imageSrc = self.filters.filterLog(self.imageSrc)
            #self.imageSrc = 255 - self.imageSrc
            pass

    def filterImagesDst(self):
        self.imageDst = cv2.resize(
            self.imageDst, (640, 480), interpolation=cv2.INTER_AREA)
        if self.whichCamera == 0:
            self.imageDst = self.filters.bilateralFilter(self.imageDst)
        if self.whichCamera == 1:
            #self.imageDst = self.filters.filterRed(self.imageDst)
            #self.imageDst = self.filters.filterLog(self.imageDst)
            #self.imageDst = 255 - self.imageDst
            pass

    def increaseProgressBar(self):
            self.countNoImageAutoAcq += 1
            value = (self.countNoImageAutoAcq/self.NoImages)*100
            self.window.progressBarExtsc.setValue(value)

    def getDrawChessBoardImages(self):
            return self.drawChessBoardImagesSource, self.drawChessBoardImagesTarget

    def getHomographyMatrix(self):
            return self.homographyMatrix

    def getImages(self):
        """
        docstring
        """
        return (self.imagesSrc, self.imagesDst)
        
