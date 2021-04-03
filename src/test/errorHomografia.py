import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

patternDimensions = [9,6]

criteria = (cv2.TERM_CRITERIA_EPS +
                 cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
TIPO_CALIB = 1
pathImagesSrc = ''
pathImagesDst = ''

if TIPO_CALIB == 0:
    homographyMatrix = np.array([
        [1.1264347327871989, -0.020191966907453385, -22.833704680474998],
        [0.012794018479444707, 1.0970015658849894, -37.00759031921894],
        [5.961239148951807e-05, -5.700641962301782e-05, 1.0]
    ])
    pathImagesSrc = '../modules/ExtrinsicCalibration/data/prueba/rgb-depth/rgb'
    pathImagesDst = '../modules/ExtrinsicCalibration/data/prueba/rgb-depth/depth'
if TIPO_CALIB == 1:
    homographyMatrix = np.array([
        [0.6871734366457675, 0.0014052801781046797, 99.59110485776192],
        [-0.00029236439381231206, 0.5845205173606985, 99.72055327863976],
        [-2.6274689270337406e-06, 4.4380963401159094e-06, 1.0]
    ])
    pathImagesSrc = '../modules/ExtrinsicCalibration/data/prueba/test2/thermal'
    pathImagesDst = '../modules/ExtrinsicCalibration/data/prueba/test2/rgb'

patternImagesSrc = glob.glob(pathImagesSrc+"/*.png")
patternImagesDst = glob.glob(pathImagesDst+"/*.png")

def rgbToDepthImage(rgbImage):
    #rgbImage = cv2.imread(relativePathRgb)
    imageDst = cv2.warpPerspective(rgbImage,
                homographyMatrix, rgbImage.shape[::-1][1:3])
    return imageDst


def findChessCorners(imageSrc, imageDst):
    corners2ImageSrc = []
    corners2ImageDst = []
    grayImageSrc = cv2.cvtColor(
            imageSrc, cv2.COLOR_BGR2GRAY)
    grayImageDst = cv2.cvtColor(
            imageDst, cv2.COLOR_BGR2GRAY)    
    retImageSrc, cornersImageSrc = cv2.findChessboardCorners(
        grayImageSrc, (patternDimensions[1], patternDimensions[0]), None)
    #print(retImageSrc)
    retImageDst, cornersImageDst = cv2.findChessboardCorners(
        grayImageDst, (patternDimensions[1], patternDimensions[0]), None)
    #print(retImageDst)

    if retImageSrc and retImageDst:
        corners2ImageSrc = cv2.cornerSubPix(
            grayImageSrc, cornersImageSrc, (11, 11), (-1, -1), criteria)
        corners2ImageDst = cv2.cornerSubPix(
            grayImageDst, cornersImageDst, (11, 11), (-1, -1), criteria)

    return (corners2ImageSrc, corners2ImageDst)

def filterRed(frame):
    frame[:, :, 0] = 150
    return frame

def filterLog(frame):
    c = 255/np.log(256)
    newFrame = c*np.log(1+frame.astype(np.float))
    newFrame = np.array(newFrame, dtype=np.uint8)
    return newFrame

def startExtrinsicCalibration(imagesSrc, imagesDst):
    pointsSrc = []
    pointsDst = []
    for which in range(len(imagesDst)):
        imageSrc = cv2.imread(imagesSrc[which])
        newRgb = rgbToDepthImage(imageSrc)
        imageDst = cv2.imread(imagesDst[which])
        # displaying image
        #cv2.imshow('imageSrc', imageSrc)
        
        #cv2.imshow('imageDst', imageDst)
        
        if TIPO_CALIB == 1:
            #red = filterRed(newRgb)
            #log = filterLog(newRgb)
            #newRgb = 255 - newRgb
            #newRgb = cv2.addWeighted(red, 1.0, newRgb, 1.0, 0)
            pass
        #cv2.imshow('newRgb', newRgb)
        #cv2.waitKey(0)
        psrc, pdst = findChessCorners(newRgb, imageDst)
        if isinstance(psrc, np.ndarray):
            pointsSrc.append(psrc)
            pointsDst.append(pdst)
        #add wait key. window waits till user press any key
    #and finally destroy/Closing all open windows
    #cv2.destroyAllWindows() 
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

pointsSrc, pointsDst = startExtrinsicCalibration(
    patternImagesSrc, patternImagesDst)
#getError(pointsSrc, pointsDst)
getResult(pointsSrc, pointsDst)
