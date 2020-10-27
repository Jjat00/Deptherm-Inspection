import numpy as np
import cv2
import os
import threading

class IntrinsicCameraCalibration():
        def __init__(self, window):
                super(IntrinsicCameraCalibration).__init__()
                self.window = window
                self.criteria = (cv2.TERM_CRITERIA_EPS +
                                 cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                self.drawChessBoardImages = []
                self.intrinsicMatrix = []
                self.distortionParameters = []
                self.countNoImageAutoAcq = 0
                self.nameImages = []
                np.set_printoptions(suppress=True)

        def setPatternDimensions(self, patternDimensions):
                self.patternDimensions = patternDimensions
                #ideal point real world
                self.objp = np.zeros(
                    (self.patternDimensions[0]*self.patternDimensions[1], 3), np.float32)
                self.objp[:, :2] = np.mgrid[0:self.patternDimensions[1],
                                            0:self.patternDimensions[0]].T.reshape(-1, 2)

        def startIntrinsicCalibration(self, pathImages):
                self.NoImages = len(pathImages)
                self.objectPoints = []
                self.imagePoints = []
                for fname in pathImages:
                        img = cv2.imread(fname)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        ret, corners = cv2.findChessboardCorners(
                            gray, (self.patternDimensions[1], self.patternDimensions[0]), flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
                        if ret == True:
                                self.nameImages.append(fname)
                                threading.Thread(target=self.increaseProgressBar).start()
                                self.objectPoints.append(self.objp)
                                corners = cv2.cornerSubPix(
                                    gray, corners, (11, 11), (-1, -1), self.criteria)
                                self.imagePoints.append(corners)
                                img = cv2.drawChessboardCorners(
                                    img, (self.patternDimensions[1], self.patternDimensions[0]), corners, ret)
                                self.drawChessBoardImages.append(img)
                                cv2.imshow('img', img)
                                cv2.waitKey(20)
                self.state, self.intrinsicMatrix, self.distortionParameters, self.rvecs, self.tvecs = cv2.calibrateCamera(
                    self.objectPoints, self.imagePoints, gray.shape[::-1], None, None)
                cv2.destroyAllWindows()

        def increaseProgressBar(self):
                self.countNoImageAutoAcq += 1
                value = (self.countNoImageAutoAcq/self.NoImages)*100
                self.window.progressBarIntrsc.setValue(value)

        def undistortImage1(self, image):
                h,  w = image.shape[:2]
                newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
                    self.intrinsicMatrix, self.distortionParameters, (w, h), 1, (w, h))
                undistImage = cv2.undistort(
                    image, self.intrinsicMatrix, self.distortionParameters, None, newcameramtx)
                # crop the image
                x, y, w, h = roi
                undistImage = undistImage[y:y+h, x:x+w]
                cv2.imwrite('calibresult1.png', undistImage)
                return undistImage

        def undistortImage2(self, image):
                h,  w = image.shape[:2]
                newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
                    self.intrinsicMatrix, self.distortionParameters, (w, h), 1, (w, h))
                mapx, mapy = cv2.initUndistortRectifyMap(
                    self.intrinsicMatrix, self.distortionParameters, None, newcameramtx, (w, h), 5)
                undistImage = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
                # crop the image
                x,y,w,h = roi
                undistImage = undistImage[y:y+h, x:x+w]
                cv2.imwrite('calibresult2.png', undistImage)
                return undistImage

        def getError(self):
                totalError = 0
                errors = []
                for i in range(len(self.objectPoints)):
                        imgpoints2, _ = cv2.projectPoints(
                            self.objectPoints[i], self.rvecs[i], self.tvecs[i], self.intrinsicMatrix, self.distortionParameters)
                        error = cv2.norm(
                            self.imagePoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
                        errors.append(error)
                        totalError += error
                error = totalError/len(self.objectPoints)

                for index in range(len(self.nameImages)):
                        print(errors[index])
                        if errors[index] > error:
                                #os.remove(self.nameImages[index])
                                pass
                return error

        def getDrawChessBoardImages(self):
                return self.drawChessBoardImages

        def getIntrinsicMatrix(self):
                return self.intrinsicMatrix

        def getDistortionParameters(self):
                return self.distortionParameters[0]
