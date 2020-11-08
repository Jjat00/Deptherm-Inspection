from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from Transformation import Transformation
import numpy as np
from vedo import *
import json
import vtk


class PointCloud1():

        def __init__(self):
                print('init PointCloud1')
                self.transformation = Transformation()

        def setRgbImage(self, rgbImage):
                self.transformation.setRgbImage(rgbImage)

        def setDepthData(self, depthData):
                self.transformation.setDepthData(depthData)

        def setColorImage(self, image):
                """
                docstring
                """
                self.colorImage = image

        def setThermalImage(self, thermalImage):
                self.transformation.setThermalImage(thermalImage)

        def getPointCloud(self):
                """
                return vertices point cloud
                """
                xyzPoints = self.transformation.depth2xyz(2.0)
                xyzColor = self.transformation.getColor()
                return xyzPoints, xyzColor

        def showPointCloud(self):
                xyzPoints, _ = self.getPointCloud()
                print('-------------------------------')
                print(len(xyzPoints))
                vertex = Points(xyzPoints, r = 1.8)#.clean(0.001)
                scalars = vertex.points()[:, 2]
                vertex.pointColors(scalars, cmap="coolwarm")
                #vertex.pointColors(scalars, cmap="binary")
                print(vertex.N())
                widgetPointCloud = self.getPointCloudWidget(vertex)
                #pointFilterd = cluster(xyzPoints, radius=0.01)
                #pointFilterd = self.knNeighbors(vertex.points(), 1)
                #pointFilterd = Points(pointFilterd, r=1.8)
                #pointFilterd.pointColors(scalars, cmap="coolwarm")
                #print(pointFilterd.N())
                print('-------------------------------')
                widgetPointCloudF = self.getPointCloudWidget(vertex)
                return widgetPointCloud, widgetPointCloudF


        def showColorPointCloud(self):
                xyzPoints = self.transformation.depth2xyz(2.0)
                xyzColor = self.transformation.getColor()
                vertex = Points(xyzPoints, r=1.8, c=xyzColor)  # .clean(0.002)
                widgetPointCloudF = self.getPointCloudWidget(vertex)
                #vertex = recoSurface(pointFilterd, dims=250, radius=0.01)
                widgetPointCloud = self.getPointCloudWidget(vertex)
                return widgetPointCloud, widgetPointCloudF

        def showThermalPointCloud(self):
                xyzPoints = self.transformation.depth2xyz(2.0)
                xyzColor = self.transformation.getTemperature()
                vertex = Points(xyzPoints, r=1.8, c=xyzColor)
                widgetPointCloud = self.getPointCloudWidget(vertex)
                return widgetPointCloud

        def setColorPointCloud(self, imageColor):
                """
                docstring
                """
                pass

        def createPointCloudWidget(self, pointCloud):
                """
                creat point cloud widget from vertices xyz points
                parameters:     
                        xyz: np.array([])
                return:
                        PointCloudWidget: QVTKRenderWindowInteractor
                """
                xyz = pointCloud['pointCloud']
                rgbImage = pointCloud['color']
                #print(rgbImage)
                print('cleaning points...')
                print(len(xyz))
                vertex = Points(xyz, r=1.8).clean(tol=0.002)
                print(vertex.N())
                #print('removing outliers...')
                #vertex = removeOutliers(vertex, 0.01, neighbors=50)
                #print(vertex.N())
                #print('clustering...')
                #cl = cluster(vertex.points(), radius=0.02)  # returns a vtkAssembly
                #vertexCluster = cl.info['clusters'][0]
                #print(len(vertexCluster))
                #self.pointCloudKN = []
                #self.knNeighbors(vertex.clone().points(),1)
                #rgb, newXYZ = self.transformation.getColorFromXYZ(np.array(self.pointCloudKN[-1]), rgbImage)
                rgb, newXYZ = self.transformation.getColorFromXYZ(vertex.points(), rgbImage)
                print('add color points...')
                # .clean(tol=0.0005)
                vertex = Points(newXYZ, r=1.8, c=rgb)
                #print(cloud0)
                #show(cloud0, interactive=1)
                #xyz = self.knNeighbors(vertex.points(),1)
                #scalars = vertex.points()[:, 2]
                #vertex.pointColors(scalars, cmap="binary")
                #vertex.pointColors(scalars, cmap="coolwarm")
                #self.toSurface(xyz)
                PointCloudWidget = self.getPointCloudWidget(vertex)
                return PointCloudWidget

        def getPointCloudWidget(self, actor):
                renderer = vtk.vtkRenderer()
                renderer.AddActor(actor)
                #renderer.SetBackground(255/255, 255/255, 255/255)
                renderer.SetBackground(13/255, 33/255, 40/255)
                renderer.ResetCamera()
                widgetPointCloud = QVTKRenderWindowInteractor()
                widgetPointCloud.Initialize()
                widgetPointCloud.Start()
                widgetPointCloud.GetRenderWindow().AddRenderer(renderer)
                return widgetPointCloud


        def toMesh(self, coords):
                print("point cloud to mesh")
                d0 = Points(coords, r=2, c="b").legend("source")
                d1 = delaunay2D(coords, mode='fit')
                d1.color("r").wireframe(True).legend("delaunay mesh")
                #cents = d1.cellCenters()
                #ap = Points(cents).legend("cell centers")
                show(d0, d1, __doc__, at=0)  # NB: d0 and d1 are slightly different
                show(d1, at=1, interactive=1)
                return d1

        def toSurface(self, pts1):
                print("point cloud to surface")
                s1 = Points(pts1, r=2, c="b").clean(tol=0.005)
                coords = s1.points()
                mesh = delaunay2D(coords, mode='fit')
                mesh.color("r").wireframe(True).legend("delaunay mesh")
                vp = Plotter(N=3, axes=0)
                vp.show(mesh, at=0)
                pts1 = s1.clone()
                #pts1 = s1.clone().smoothMLS2D(f=0.8)  # smooth cloud
                print("Nr of points before cleaning nr. points:", pts1.N())
                # impose a min distance among mesh points
                pts1.clean(tol=0.0015).legend("smooth cloud")
                print("             after  cleaning nr. points:", pts1.N())
                vp.show(pts1, at=1)
                # reconstructed surface from point cloud
                reco = recoSurface(pts1, dims=200, radius=0.01).legend("surf. reco")
                vp.show(reco, at=2, axes=7, zoom=1.2, interactive=1)

        def knNeighbors(self, vertices, nIteration):
                print(len(vertices))
                vertices = Points(vertices).clean(0.002)
                #vertices = Points(vertices)
                nIteration = nIteration-1
                if nIteration >= 0:
                        print(nIteration)
                        newPointCloud = []
                        for i in range(vertices.N()):
                                pt = vertices.points()[i]
                                ids = vertices.closestPoint(pt, N=10, returnIds=True)
                                newPointCloud.append(
                                        np.mean(vertices.points()[ids], axis=0).tolist())
                        newPointCloud = np.array(newPointCloud)
                        self.pointCloudKN.append(newPointCloud)
                        self.knNeighbors(newPointCloud, nIteration)


        def centerPlane(self, vertices, nIteration):
                nIteration = nIteration-1
                vertices = Points(vertices)#.clean(tol=0.0001)
                if nIteration >= 0:
                        print(nIteration)
                        points = []
                        for i, p in enumerate(vertices.points()):
                                pts = vertices.closestPoint(p, N=10)
                                plane = fitPlane(pts)             # find the fitting plane
                                points.append(plane.center)
                        points = np.array(points)
                        self.centerPlane(points, nIteration)
                        return points
