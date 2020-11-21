"""
File: Transformation.py
Author: Jaime Aza <<Jjat: userjjat00@gmail.com>>
Date create: 02-oct-2020
"""
import numpy as np
import cv2

relativePathRgb = 'modules/InspectionAnalyzer/data/images/rgbImage.png'
relativePathDepth = 'modules/InspectionAnalyzer/data/images/depthImage.png'
relativePathThermal = 'modules/InspectionAnalyzer/data/images/thermalImage.png'
relativePathColor = 'modules/InspectionAnalyzer/data/images/colorImage.png'

class Transformation():
        def __init__(self):
                print('init Transformation')
                self.intrinsicMatrix = []
                self.homographyRgbToDepth = []
                self.homographyThermalToRgb = []

                self.setIntrinsicMatrix()
                self.setHomographyRgbToDepth()
                self.setHomographyThermalToRgb()

        def setDepthData(self, depthData):
                #self.depthData = depthData[::2, ::2]
                self.depthData = depthData

        def setDepthImage(self, depthImage):
                cv2.imwrite(relativePathDepth, depthImage)

        def setRgbImage(self, rgbImage):
                cv2.imwrite(relativePathRgb, rgbImage)

        def setThermalImage(self, thermalImage):
                cv2.imwrite(relativePathThermal, thermalImage)

        def setColorImage(self, colorImage):
                """
                docstring
                """
                cv2.imwrite(relativePathColor, colorImage)

        def setIntrinsicMatrix(self):
                #intrinsicMatrix = np.array([
                #    [570.5725384259518, 0.0, 335.17270110938176],
                #    [0.0, 570.5544526637268, 246.2629901893306],
                #    [0.0, 0.0, 1.0]
                #])
                intrinsicMatrix = np.array([
                    [563.076178, 0.0, 337.440465],
                    [0.0, 566.767587, 237.610503],
                    [0.0, 0.0, 1.0]
                ])

                self.intrinsicMatrix = intrinsicMatrix

        def setHomographyRgbToDepth(self):

                #homographyMatrix = np.array([
                #    [1.0819969500137874, 0.017251494265154415, -20.626941586246897],
                #    [-0.012360766358243186, 1.1152452865213556, -33.18791897305533],
                #    [-6.724964767791937e-05, 6.627478506708851e-05, 1.0]
                #])

                homographyMatrix = np.array([
                    [1.1264347327871989, -0.020191966907453385, -22.833704680474998],
                    [0.012794018479444707, 1.0970015658849894, -37.00759031921894],
                    [5.961239148951807e-05, -5.700641962301782e-05, 1.0]
                ])

                self.homographyRgbToDepth = homographyMatrix

        def setHomographyThermalToRgb(self):
                #homographyMatrix = np.array([
                #    [0.29424046705638934, 0.0037388668083184816, 209.94738315208423],
                #    [-0.004277747148311227, 0.30976870602627143, 144.43526131626922],
                #    [-5.078621245575828e-05, 2.7181668475245755e-05, 1.0]
                #])
                homographyMatrix = np.array([
                    [0.6854801, -0.00008356, 100.13680033],
                    [-0.00031612, 0.58269707, 99.85123366],
                    [-0.00000309, -0.00000037, 1.0]
                ])
                self.homographyThermalToRgb = homographyMatrix

        def rgbToDepthImage(self):
                rgbImage = cv2.imread(relativePathRgb)
                imageDst = cv2.warpPerspective(rgbImage,
                        self.homographyRgbToDepth, rgbImage.shape[::-1][1:3])
                return imageDst

        def colorToDepthImage(self):
                rgbImage = cv2.imread(relativePathColor)
                imageDst = cv2.warpPerspective(rgbImage,
                        self.homographyRgbToDepth, rgbImage.shape[::-1][1:3])
                return imageDst

        def thermalToDepthImage(self):
                thermalImage = cv2.imread(relativePathThermal)
                imageDst = cv2.warpPerspective(thermalImage,
                        self.homographyThermalToRgb, thermalImage.shape[::-1][1:3])
                imageDst = cv2.warpPerspective(imageDst,
                        self.homographyRgbToDepth, imageDst.shape[::-1][1:3])
                return imageDst

        def thermalToRgbImage(self):
                thermalImage = cv2.imread(relativePathThermal)
                imageDst = cv2.warpPerspective(thermalImage,
                        self.homographyThermalToRgb, thermalImage.shape[::-1][1:3])
                return imageDst

        def depthToRgbImage(self):
                depthImage = cv2.imread(relativePathDepth)
                imageDst = cv2.warpPerspective(depthImage,
                        np.linalg.inv(self.homographyRgbToDepth), depthImage.shape[::-1][1:3])
                return imageDst

        def depth2xyz(self, depth):
                u, v = np.mgrid[:480, :640]
                #u, v = np.mgrid[:480:2, :640:2]
                self.zWorld =  0.1236 * np.tan((self.depthData.flatten()/2842.5) + 1.1863)-0.037
                uvs = np.vstack((self.zWorld *u.flatten(), self.zWorld *v.flatten(), self.zWorld ))
                xyz = np.dot(np.linalg.inv(self.intrinsicMatrix), -uvs).transpose()[self.zWorld>0]
                self.mask = self.zWorld[self.zWorld>0]
                newXyz = xyz[self.mask < depth]
                return newXyz

        def xyz2uv(self, xyz: np.array):
                """
                transform xyz cooirdintes to uv coordinates
                patameters: 
                        xyz: is a point cloud
                return:
                        u, v: is a coordinates (u,v) of image 
                """
                print('transform xyz cooirdintes to uv coordinates...')
                x = xyz[:,0]
                y = xyz[:,1]
                z = xyz[:,2]
                newXYZ = np.vstack((x, y, z))
                u, v, w = np.dot(self.intrinsicMatrix, -newXYZ)

                u = np.int_(np.round(u/w))
                v = np.int_(np.round(v/w))

                return u, v

        def getColorFromXYZ(self, xyz, rgbImage):
                """
                get RGB color from xyz coordinates
                Parameters:
                        xyz: coordinates of point cloud
                        rgbImage: image correponding to point cloud
                return:
                        rgb: new rgb coordinates
                """
                u, v = self.xyz2uv(xyz)

                newXYZ = xyz[np.array(u < 480)*np.array(v < 640)]
                newU = u[np.array(u < 480)*np.array(v < 640)]
                newV = v[np.array(u < 480)*np.array(v < 640)]

                b = rgbImage[newU, newV, 0].flatten()
                g = rgbImage[newU, newV, 1].flatten()
                r = rgbImage[newU, newV, 2].flatten()

                rgb = np.vstack((r, g, b)).T

                return rgb, newXYZ

        def getColorRgb(self):
                rgbImage = self.rgbToDepthImage()
                #rgbImage = rgbImage[::2, ::2]
                #width, heigth, _ = rgbImage.shape
                #b = rgbImage[0:width, 0:heigth, 0].flatten()
                #g = rgbImage[0:width, 0:heigth, 1].flatten()
                #r = rgbImage[0:width, 0:heigth, 2].flatten()
                #rgb = np.vstack((r,g,b)).T[self.zWorld>0]
                #newRgb = rgb[self.mask < 1.5]
                return rgbImage

        def getColor(self):
                rgbImage = self.colorToDepthImage()
                return rgbImage
                
        def getTemperature(self):
                newThermal = self.thermalToDepthImage()
                #width, heigth, _ = newThermal.shape
                #b = newThermal[0:width, 0:heigth, 0].flatten()
                #g = newThermal[0:width, 0:heigth, 1].flatten()
                #r = newThermal[0:width, 0:heigth, 2].flatten()
                #thermal = np.vstack((r, g, b)).T[self.zWorld > 0]
                #newThermal = thermal[self.mask < 1.5]
                return newThermal


""" 
    def configTransformation(self):
        strIntrinsic = self.window.textBrowserIntrinsic.toPlainText()
        intrinsicMatrix = np.array(json.loads(strIntrinsic))

        strHomograhpyR2D = self.window.textBrowserH1.toPlainText()
        homograhpyR2D = np.array(json.loads(strHomograhpyR2D))

        strHomograhpyT2D = self.window.textBrowserH2.toPlainText()
        homograhpyT2D = np.array(json.loads(strHomograhpyT2D))

        return intrinsicMatrix, homograhpyR2D, homograhpyT2D
"""
