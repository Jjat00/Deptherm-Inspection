import glob
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


def thermal2rgbImage(thermalImage):
    homographyThermalToRgb = np.array([
        [0.7402546641601684, -0.012460486372473198, 47.70461031588572],
        [0.019926646975580414, 0.604406915907843, 98.1984254265369],
        [5.5850994711816295e-05, -2.0667286302057624e-05, 1.0]
    ])
    imageDst = cv2.warpPerspective(thermalImage,
                                   homographyThermalToRgb, thermalImage.shape[::-1][1:3])

    return imageDst


def findChessCorners(imageSrc, imageDst):
    find = False
    #cv2.imshow('thermalImage', imageSrc)
    #cv2.imshow('thermal2depth', imageDst)
    #cv2.waitKey(0)
    patternDimensionsSrc = [9, 6]
    criteria = (cv2.TERM_CRITERIA_EPS +
                cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners2ImageSrc = []
    corners2ImageDst = []

    grayImageSrc = cv2.cvtColor(
        imageSrc, cv2.COLOR_BGR2GRAY)
    grayImageDst = cv2.cvtColor(
        imageDst, cv2.COLOR_BGR2GRAY)

    retImageSrc, cornersImageSrc = cv2.findChessboardCorners(
        grayImageSrc, (patternDimensionsSrc[1], patternDimensionsSrc[0]), cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FILTER_QUADS)
    patternDimensionsDst = [9, 6]
    retImageDst, cornersImageDst = cv2.findChessboardCorners(
        grayImageDst, (patternDimensionsDst[1], patternDimensionsDst[0]), cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FILTER_QUADS)
    if retImageSrc and retImageDst:
        corners2ImageSrc = cv2.cornerSubPix(
            grayImageSrc, cornersImageSrc, (11, 11), (-1, -1), criteria)
        corners2ImageDst = cv2.cornerSubPix(
            grayImageDst, cornersImageDst, (11, 11), (-1, -1), criteria)

        grayImageSrc = cv2.cvtColor(
            grayImageSrc, cv2.COLOR_GRAY2BGR)
        imageDraw1 = cv2.drawChessboardCorners(
            grayImageSrc, (patternDimensionsSrc[1], patternDimensionsSrc[0]),
            corners2ImageSrc, retImageSrc)

        grayImageDst = cv2.cvtColor(
            grayImageDst, cv2.COLOR_GRAY2BGR)
        imageDraw2 = cv2.drawChessboardCorners(
            grayImageDst, (patternDimensionsDst[1], patternDimensionsDst[0]),
            corners2ImageDst, retImageDst)

        #cv2.imshow('thermalImage', imageDraw1)
        #cv2.imshow('thermal2depth', imageDraw2)
        #cv2.waitKey(0)
    return (corners2ImageSrc, corners2ImageDst)


def startFindCorners(imagesSrc, imagesDst):
    pointsSrc = []
    pointsDst = []
    for which in range(len(imagesDst)):
        imageSrc = cv2.imread(imagesSrc[which])
        newImage = thermal2rgbImage(imageSrc)
        imageDst = cv2.imread(imagesDst[which])
        psrc, pdst = findChessCorners(newImage, imageDst)
        if isinstance(psrc, np.ndarray):
            pointsSrc.append(psrc)
            pointsDst.append(pdst)

    return (pointsSrc, pointsDst)


def getError(pointSrc, pointDst):
    totalError = 0
    errors = []
    for i in range(len(pointDst)):
        error = cv2.norm(
            pointSrc[i], pointDst[i], cv2.NORM_L2)/len(pointDst)
        errors.append(error)
        totalError += error
    error = totalError/len(errors)
    for index in range(len(errors)):
            print(errors[index])
            if errors[index] > error:
                    pass
    return (error, errors)


def getResult(pointsSrc, pointsDst):
    totalError, errors = getError(pointsSrc, pointsDst)
    print('total error: ', totalError)
    print(errors)
    nImages = np.linspace(0, len(errors)-1,  len(errors))
    print(nImages)
    plt.plot(nImages, errors)
    plt.title('Error de proyección')
    plt.xlabel('frame', fontsize=16)
    plt.ylabel('error', fontsize=16)
    plt.grid()
    plt.show()


def emulatedThermalImage(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = abs(255 - frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    return frame

def setMaxUmbral(imageToAnalyzer, maxUmbral):
    """
    docstring
    """
    image = cv2.cvtColor(imageToAnalyzer, cv2.COLOR_RGB2GRAY)
    res, mask = cv2.threshold(image, maxUmbral, 255, cv2.THRESH_BINARY_INV)
    FalseColorImage = cv2.applyColorMap(image, cv2.COLORMAP_MAGMA)
    falseColor = cv2.bitwise_or(
        FalseColorImage, FalseColorImage, mask=mask)
    return falseColor

def viewImages():
    image = cv2.imread('images/thermal/image41.png')
    newImage = thermal2rgbImage(image)
    newImage = emulatedThermalImage(newImage)
    newImage = setMaxUmbral(newImage, 254.999999)
    rgbImage = cv2.imread('images/rgb/image41.png')
    fusionImage = cv2.addWeighted(
        rgbImage, 40 / 100, newImage, 100 / 100, 0)
    thermalImage = emulatedThermalImage(image)
    thermalImage = cv2.applyColorMap(thermalImage, cv2.COLORMAP_MAGMA)
    cv2.imshow('thermalImage', thermalImage)
    cv2.imshow('rgbImage', rgbImage)
    cv2.imshow('fusionImage', fusionImage)

    cv2.waitKey(0)


if __name__ == "__main__":
    viewImages()
    #pathThermalImage = 'images/thermal'
    #pathRgbImage = 'images/rgb'
    #patternImagesSrc = glob.glob(pathThermalImage+"/*.png")
    #patternImagesDst = glob.glob(pathRgbImage+"/*.png")
    #pointsSrc, pointsDst = startFindCorners(patternImagesSrc, patternImagesDst)
    #getResult(pointsSrc, pointsDst)
    #for i in range(3,50):
    #print('images/thermal/image%i.png' % i)
    #thermalImage = cv2.imread('images/thermal/image%i.png' % i)
    #thermal2depthImage = thermal2rgbImage(thermalImage)
    #rgbImage = cv2.imread('images/depth/image%i.png' % i)
    #find = findChessCorners(thermal2depthImage, rgbImage)
    #if not find:
    #    print('eliminar imagen')
    #    os.remove('images/thermal/image%i.png' % i)
    #    os.remove('images/depth/image%i.png' % i)
