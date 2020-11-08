from vedo import Points
import numpy as np

class Registration():
    """
    Aligned n frames RGBD camera
    """
    def __init__(self):
        print('init Registration')

    def setPointCloud(self, groupPointCloud):
        """
        parameters:
            groupPointCloud:
                    groupPointCloud['vertex']: list vertex point cloud
                    groupPointCloud['color']: list color vertex point cloud

        """
        self.groupPointCloud = groupPointCloud['vertex']
        self.groupColorPoint = groupPointCloud['color']


    def initICP(self):
        """
        start alignment
        """
        self.totalAlinedPoints = []  # to store the final cloud
        self.totalAlinedDifferencePoints = []  # to store the difference of each cloud

        #self.runiCP(self.groupPointCloud, len(self.groupPointCloud))
        self.runICP2(self.groupPointCloud)
                
        groupTotalPoint = []
        #groupTotalDifferencePoint = []
        print('total point cloud aligned', len(self.totalAlinedPoints))
        for index in range(len(self.totalAlinedPoints)):
            groupTotalPoint = groupTotalPoint + self.totalAlinedPoints[index].tolist()
            #groupTotalDifferencePoint = groupTotalDifferencePoint + self.totalAlinedDifferencePoints[index].tolist()
        print('groupTotalPoint:')
        print(len(groupTotalPoint))
        #print('groupTotalDifferencePoint:')
        #print(len(groupTotalDifferencePoint))
        
        pointCloudAligend = {
            'pointCloud': groupTotalPoint,
            'color': self.groupColorPoint[0],
        }
        return pointCloudAligend


    def runiCP(self, groupPointCloud, nIterations):
        """
        start icp
        """
        print('No nubes: ')
        print(len(groupPointCloud))
        groupPointAux = []  # para almacenar nubes temporales
        nIterations = nIterations - 1
        print('iteration: ', nIterations)
        if nIterations > 1:

            alignedPoint, differencePoint = self.aligned(groupPointCloud[1], groupPointCloud[0])
            groupPointAux.append(alignedPoint)
            self.totalAlinedPoints.append(alignedPoint)
            self.totalAlinedDifferencePoints.append(differencePoint)

            print('aligned:')
            for index in range(len(groupPointCloud)-2):
                print(index)
                verticesSorce = groupPointCloud[index+2]
                verticesDst = groupPointCloud[index+1]
                alignedPoint, differencePoint = self.aligned(verticesSorce, verticesDst)
                groupPointAux.append(alignedPoint)

            self.runiCP(groupPointAux, nIterations)

        else:
            self.totalAlinedPoints.append(groupPointCloud[0])
            self.totalAlinedDifferencePoints.append(groupPointCloud[0])


    def runICP2(self, groupPointCloud):
        """
        docstring
        """
        if len(groupPointCloud) > 1:
            alignedPoint = self.aligned(groupPointCloud[1], groupPointCloud[0])
            alignedPoint, differencePoint = self.aligned(groupPointCloud[1], groupPointCloud[0])
            self.totalAlinedPoints.append(alignedPoint)
            print('aligned:')
            for index in range(len(groupPointCloud)-2):
                print(index)
                verticesSorce = groupPointCloud[index+2]
                verticesDst = self.totalAlinedPoints[index]
                alignedPoint, differencePoint = self.aligned(verticesSorce, verticesDst)
                self.totalAlinedPoints.append(alignedPoint)
        else:
            self.totalAlinedPoints.append(groupPointCloud[0])


    def aligned(self, sourcePoints, destinationPoints):
        """
        Aligned two points cloud
        Parameters:
            sorucePoints: np.array()
            destinationPoints: np.array()
        return:
            alignedPoints: Points
        """
        verticesSourcePoints = Points(sourcePoints, r=1.0, c="b")
        verticesDestinationPoints = Points(destinationPoints, r=1.0, c="g")
        print("align..")
        alignedPoints = verticesSourcePoints.alignTo(verticesDestinationPoints, iters=200)
        differencePoint = self.getDifference(
            verticesDestinationPoints.points(), alignedPoints.points())
        return alignedPoints.points(), differencePoint


    def getDifference(self, sourcePoints, destinationPoints):
        """
        Get  difference between sourcePoints and destinationPoints
        """
        difference = sourcePoints - destinationPoints
        differenceTotal = np.mean(difference, axis=1)
        maskValidPoints = np.absolute(differenceTotal) > 0.15
        destinationPointsAux = destinationPoints[maskValidPoints]
        return destinationPointsAux
