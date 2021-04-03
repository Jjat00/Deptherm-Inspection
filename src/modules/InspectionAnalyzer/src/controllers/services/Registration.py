from numpy.core.fromnumeric import size
from vedo import *
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

        """         nuevoGrupo = []
        for point in self.groupPointCloud:
            points = self.planeSegmentation(point)
            nuevoGrupo.append(points)

        LengthPointCloud = []
        for grupo in nuevoGrupo:
            LengthPointCloud.append(len(grupo))

        minLengthPoint = np.amin(LengthPointCloud)
        coordinates = []
        color = []

        for index in range(len(nuevoGrupo)):
            coordinatesAux = np.array(nuevoGrupo[index])
            colorAux = np.array(self.groupColorPoint[index])
            coordinates.append(coordinatesAux[0:minLengthPoint, :])
            color.append(colorAux[0:minLengthPoint, :])

        self.groupPointCloud = coordinates
        self.groupColorPoint = color  """
        


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
        
        plt = Plotter(shape=(1, 2))
        newgroupTotalPoint = Points(groupTotalPoint, r=2)#.clean(0.001)
        #newgroupTotalPoint = Points(newgroupTotalPoint, r=3)
        scalars = newgroupTotalPoint.points()[:, 2]
        newgroupTotalPoint.pointColors(scalars, cmap="jet")
        #vp.show(newgroupTotalPoint, viewup='z')
        plt.show(newgroupTotalPoint, at=0)
        write(newgroupTotalPoint, 'modules/InspectionAnalyzer/data/test_pc.ply')
        newgroupTotalPoint = Points(
            self.totalAlinedPoints[0], r=2)#.clean(0.001)
        #newgroupTotalPoint = Points(
        #    newgroupTotalPoint, r=3)
        scalars = newgroupTotalPoint.points()[:, 2]
        newgroupTotalPoint.pointColors(scalars, cmap="jet")
        
        plt.show(newgroupTotalPoint, at=1, interactive=True)
        pointCloudAligend = {
            'pointCloud': groupTotalPoint,
            'color': self.groupColorPoint[1],
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
            self.totalAlinedDifferencePoints.append(differencePoint)
            print('aligned:')
            for index in range(len(groupPointCloud)-2):
                print(index)
                verticesSorce = groupPointCloud[index+2]
                verticesDst = self.totalAlinedPoints[index]
                alignedPoint, differencePoint = self.aligned(verticesSorce, verticesDst)
                self.totalAlinedPoints.append(alignedPoint)
                self.totalAlinedDifferencePoints.append(differencePoint)
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

    def planeSegmentation(self, xyzPoints):
        auxPoints = Points(xyzPoints).clean(0.004)
        points = Points(xyzPoints[::2, :]).clean(0.004)
        print(points.N())
        plane = fitPlane(points)
        print('plane')
        print(plane.points())
        print('normal')
        print(plane.normal)
        print('dir normal')
        print(np.average(plane.normal))
        pts = plane.points()[0]
        d = - plane.normal[0]*pts[0] - \
            plane.normal[1]*pts[1] - plane.normal[2]*pts[2]
        arrows = Arrow(plane.center, plane.center+plane.normal/5)
        newPoints = []
        for pts in auxPoints.points():
                distancePoint = plane.normal[0]*pts[0] + \
                    plane.normal[1]*pts[1]+plane.normal[2]*pts[2] + d
                if np.average(plane.normal) > 0:
                        if distancePoint > 0.01:
                                newPoints.append(pts)
                else:
                        if distancePoint < -0.01:
                                newPoints.append(pts)
        points = Points(newPoints)
        show(points, plane, arrows, viewup='z')
        return newPoints
