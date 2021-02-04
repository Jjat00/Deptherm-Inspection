import matplotlib.pyplot as plt
import numpy as np
import cv2
from numpy.core.fromnumeric import _partition_dispatcher


def emultaedThermalImage(rgbImage):
    height, width = rgbImage.shape[:2]
    crop_img = rgbImage[100:height-100, 100:width-100]
    newImage = cv2.resize(
            crop_img, (int(width), int(height)), cv2.INTER_CUBIC)        
    return newImage

def thermalToDepthImage(thermalImage):
    homographyThermalToRgb = np.array([
        [0.6871734366457675, 0.0014052801781046797, 99.59110485776192],
        [-0.00029236439381231206, 0.5845205173606985, 99.72055327863976],
        [-2.6274689270337406e-06, 4.4380963401159094e-06, 1.0]
    ])
    homographyRgbToDepth = np.array([
        [1.1264347327871989, -0.020191966907453385, -22.833704680474998],
        [0.012794018479444707, 1.0970015658849894, -37.00759031921894],
        [5.961239148951807e-05, -5.700641962301782e-05, 1.0]
    ])

    imageDst = cv2.warpPerspective(thermalImage,
                                   homographyThermalToRgb, thermalImage.shape[::-1][1:3])
    imageDst = cv2.warpPerspective(imageDst,
                                   homographyRgbToDepth, imageDst.shape[::-1][1:3])
    return imageDst


def findChessCorners(imageSrc, imageDst):
    patternDimensionsSrc = [7, 6]
    criteria = (cv2.TERM_CRITERIA_EPS +
                cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners2ImageSrc = []
    corners2ImageDst = []

    grayImageSrc = cv2.cvtColor(
        imageSrc, cv2.COLOR_BGR2GRAY)
    grayImageDst = cv2.cvtColor(
        imageDst, cv2.COLOR_BGR2GRAY)

    retImageSrc, cornersImageSrc = cv2.findChessboardCorners(
        grayImageSrc, (patternDimensionsSrc[1], patternDimensionsSrc[0]), cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_ADAPTIVE_THRESH  + cv2.CALIB_CB_FILTER_QUADS)

    patternDimensionsDst = [9, 6]
    retImageDst, cornersImageDst = cv2.findChessboardCorners(
        grayImageDst, (patternDimensionsDst[1], patternDimensionsDst[0]), cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_ADAPTIVE_THRESH  + cv2.CALIB_CB_FILTER_QUADS)

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

    newCornersSrc = corners2ImageSrc
    newCornersDst = corners2ImageDst[:-12]

    #patternDimensionsDst = [7,6]
    grayImageDst = cv2.cvtColor(
        grayImageDst, cv2.COLOR_GRAY2BGR)        
    #imageDraw2 = cv2.drawChessboardCorners(
    #    grayImageDst, (patternDimensionsDst[1], patternDimensionsDst[0]),
    #    newCornersDst, retImageDst)

    for i in newCornersDst:
        x, y = i.ravel()
        cv2.circle(grayImageDst, (x, y), 3, (0, 0, 255), -1)
    for i in newCornersSrc:
        x, y = i.ravel()
        cv2.circle(grayImageDst, (x, y), 3, (50, 200, 50), -1)

    #cv2.imshow('imageDraw1', imageDraw1)
    #cv2.imshow('imageDraw2', grayImageDst)
    #cv2.waitKey(0)

    return (newCornersSrc, newCornersDst)


def startFindCorners(imagesSrc, imagesDst):
    pointsSrc = []
    pointsDst = []
    for which in range(len(imagesDst)):
        imageSrc = cv2.imread(imagesSrc[which])
        thermalImage = emultaedThermalImage(imageSrc)
        newImage = thermalToDepthImage(thermalImage)
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
                    #os.remove(nameImages[index])
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

if __name__ == "__main__":
    import glob

    pathThermalImage = '../modules/ExtrinsicCalibration/data/prueba/test2/thermal'
    pathRgbImage = 'imagesErrorProyeccion/im2/rgb'
    pathDepthImage = 'imagesErrorProyeccion/im2/depth'

    patternImagesSrc = glob.glob(pathRgbImage+"/*.png")
    patternImagesDst = glob.glob(pathDepthImage+"/*.png")

    pointsSrc, pointsDst = startFindCorners(patternImagesSrc, patternImagesDst)
    getResult(pointsSrc, pointsDst)

    #rgbImage = cv2.imread(pathRgbImage + '/image9.png')
    #depthImage = cv2.imread(pathDepthImage + '/image9.png')

    #emultaedThermalImage = emultaedThermalImage(rgbImage)
    #newImage = thermalToDepthImage(emultaedThermalImage)
    #fusion = depthImage + newImage

    #findChessCorners(newImage, depthImage)

    #cv2.imshow('thermal image', emultaedThermalImage)
    #cv2.imshow('new image', newImage)
    #cv2.imshow('image dst', depthImage)
    #cv2.imshow('fusion', fusion)
    #cv2.waitKey(0)
