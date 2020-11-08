import cv2
import numpy as np
from matplotlib import pyplot as plt


class Analyzer():
    """
    docstring
    """
    def __init__(self):
        print('init Analyzer')
        self.nameColor = ''

    def setImageToAnalyzer(self, imageToAnalyzer):
        """
        parameters:
            image: thermal image
        """
        self.imageToAnalyzer = imageToAnalyzer

    def setRgbImage(self, rgbImage):
        """
        parameters:
            image: thermal image
        """
        self.rgbImage = rgbImage

    def setFalseColor(self, nameColor):
        """
        parameters:
            nameColor: name color -> 'jet', 'rainbow', 'hsv'
        """
        self.nameColor = nameColor
        image = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        self.falseColor = self.getFalseColorImage(image)

    def getFalseColorImage(self, grayImage):
        """
        docstring
        """
        print('color: ', self.nameColor)
        if self.nameColor == 'rainbow':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_RAINBOW)
        if self.nameColor == 'jet':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_JET)
        if self.nameColor == 'hsv':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_HSV)
        if self.nameColor == 'magma':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_MAGMA)
        if self.nameColor == 'rainbow-inv':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_RAINBOW)
            newImage = abs(255 - newImage)
        if self.nameColor == 'winter':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_WINTER)
        if self.nameColor == 'summer':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_SUMMER)
        if self.nameColor == 'cool':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_COOL)
        if self.nameColor == 'pink':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_PINK)
        if self.nameColor == 'hot':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_HOT)
        if self.nameColor == 'parula':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_PARULA)
        if self.nameColor == 'inferno':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_INFERNO)
        if self.nameColor == 'plasma':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_PLASMA)
        if self.nameColor == 'viridis':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_VIRIDIS)
        if self.nameColor == 'turbo':
            newImage = cv2.applyColorMap(grayImage, cv2.COLORMAP_TURBO)
        if self.nameColor == '':
            newImage = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2RGB)
        return newImage

    def setMaxUmbral(self, maxUmbral):
        """
        docstring
        """
        image = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        res, mask = cv2.threshold(image, maxUmbral, 255, cv2.THRESH_BINARY)
        FalseColorImage = self.getFalseColorImage(image)
        self.falseColor = cv2.bitwise_or(
            FalseColorImage, FalseColorImage, mask=mask)
        return self.falseColor

    def setMinUmbral(self, minUmbral):
        """
        docstring
        """

        image = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        t, maskMin = cv2.threshold(image, minUmbral, 255, cv2.THRESH_BINARY_INV)
   
        FalseColorImage = self.getFalseColorImage(image)

        self.falseColor = cv2.bitwise_or(
            FalseColorImage, FalseColorImage, mask=maskMin)
        return self.falseColor

    def setMinMaxUmbral(self, minUmbral, maxUmbral):
        """
        docstring
        """
        image = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        t, maskMin = cv2.threshold(
            image, minUmbral, 255, cv2.THRESH_BINARY_INV)

        t, maskMax = cv2.threshold(image, maxUmbral, 255, cv2.THRESH_BINARY)
        FalseColorImage = self.getFalseColorImage(image)

        mask = maskMin + maskMax

        self.falseColor = cv2.bitwise_or(
            FalseColorImage, FalseColorImage, mask=mask)
        return self.falseColor

    def getFalseColor(self):
        """
        docstring
        """
        #image = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        #FalseColorImage = self.getFalseColorImage(image)
        return self.falseColor

    def getFusionImage(self, visibThermal, visibRgb):
        """
        docstring
        """
        image = cv2.addWeighted(self.falseColor, visibThermal / 100,
                                self.rgbImage, visibRgb / 100, 0)
        return image

    def ecualizarHistograma(self):
        """
        docstring
        """
        pass

    def bordes(self):
        """
        docstring
        """
        pass

    def area(self):
        """
        docstring
        """
        pass

    def histograma(self):
        """
        docstring
        """
        img = cv2.cvtColor(self.imageToAnalyzer, cv2.COLOR_RGB2GRAY)
        hist, bins = np.histogram(img.flatten(), 256, [0, 256])
        #cv2.imshow('image', self.imageToAnalyzer)
        plt.hist(img.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.show()

    def paletaColor(self):
        """
        docstring
        """
        pass

    def gradoTransferencia(self):
        """
        docstring
        """
        pass

    def gradoTransferencia(self):
        """
        docstring
        """
        pass
