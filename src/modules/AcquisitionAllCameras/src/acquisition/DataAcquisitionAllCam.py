import freenect
import numpy as np
import cv2

class DataAcquisitionAllCam():
        """
        Class for handling cameras: Kinect camera and FLIR thermal camera
        """

        def __init__(self):
                super(DataAcquisitionAllCam).__init__()

        def getDepthImage(self):
                """
                Get Depth image, this transform depth data to depth image of 8 bits
                return:
                        depthImage: gray image
                """
                self.depthData, _ = freenect.sync_get_depth()
                self.depthImage = self.depthData.astype(np.uint8)
                self.depthImage = cv2.cvtColor(
                    self.depthImage, cv2.COLOR_GRAY2BGR)
                return self.depthImage

        def getDepthData(self):
                """ 
                Get depth data from kinect camera
                return:
                        depthData: np.array dimensions (640,480) each coordiante (u,v)
                        has a depth data of 11 bits
                """
                return self.depthData
                
        def getRgbImage(self):
                """
                Get rgb image from kinect camera
                return:
                        rgbImage: rgb image
                """
                self.rgbImage, _  = freenect.sync_get_video()
                self.rgbImage = cv2.cvtColor(self.rgbImage, cv2.COLOR_RGB2BGR)
                return self.rgbImage

        def getThermalImage(self):
                """
                Get thermal image from FLIR 320 thermal camera
                return:
                        thermalImage: thermal image
                """
                #ret, self.thermalImage = self.thermalCamera.read()
                self.thermalImage = self.getRgbImage()
                self.thermalImage = self.zoom(self.thermalImage)
                #self.thermalImage = self.rotation(self.thermalImage)
                return self.thermalImage

        def rotation(self, image):
                ancho = image.shape[1]  # columnas
                alto = image.shape[0]  # filas}
                # Rotación
                M = cv2.getRotationMatrix2D((ancho//2, alto//2), 180, 1)
                #M = cv2.getRotationMatrix2D((317.03,237.62),180,1)
                image = cv2.warpAffine(image, M, (ancho, alto))
                return image

        def captureRgbImage(self):
                """
                Capture rgb image obtained from kinect camera
                return:
                        rgbImageCaptured: rgb image
                """
                self.rgbImageCaptured = self.rgbImage
                return self.rgbImageCaptured

        def captureDepthImage(self):
                """
                Capture depth image obtained from kinect camera
                return:
                        rgbImageCaptured: gray image
                """
                self.depthImageCaptured = self.depthImage
                self.depthDataCaptured = self.depthData
                return self.depthImageCaptured

        def captureThermalImage(self):
                """
                Capture thermal image obtained from FLIR thermal camera
                return:
                        rgbImageCaptured: rgb image
                """
                self.thermalImageCaptured = self.thermalImage
                return self.thermalImageCaptured
                
        def saveRgbImage(self, nameImage):         
                """
                Save captured rgb image 
                paramters:
                        nameImage: path to save image and name image
                """
                cv2.imwrite(nameImage, self.rgbImageCaptured)

        def saveDepthImage(self, nameImage):
                """
                Save captured depth image
                paramters:
                        nameImage: path to save image and name image
                """
                np.save(nameImage, self.depthDataCaptured)
                cv2.imwrite(nameImage, self.depthImageCaptured)

        def saveThermalImage(self, nameImage):                
                """
                Save captured thermal image
                paramters:
                        nameImage: path to save image and name image
                """
                cv2.imwrite(nameImage, self.thermalImageCaptured)

        def initThermalCamera(self):
                """ 
                Set the camera number detected on the computer
                example:
                        cv2.VideoCapture().open(0) -> get webcam computer camera
                        cv2.VideoCapture().open(1) -> get thermal camera
                """
                print("init thermal camera...")
                self.thermalCamera = cv2.VideoCapture()
                self.thermalCamera.open(0)
                #self.thermalCamera.open(
                #    'http://192.168.1.4:4747/videostream.cgi?.mjpg')
                #pass

        def closeThermalCamera(self):
                """
                docstring
                """
                print("closing thermal camera...")
                self.thermalCamera.release()
                #pass


        def zoom(self, image):
                height, width = image.shape[:2]
                crop_img = image[100:height-100, 100:width-100]

                newImage = cv2.resize(
                        crop_img, (int(width), int(height)), cv2.INTER_CUBIC)
                        
                return newImage
