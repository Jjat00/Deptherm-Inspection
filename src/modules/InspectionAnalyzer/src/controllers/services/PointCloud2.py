from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide2.QtWidgets import QApplication
from Transformation import Transformation
import numpy as np
from vedo import *
import json
import vtk


class PointCloud2():

        def __init__(self):
            print('init PointCloud2')
            self.transformation = Transformation()
            self.pointCloud = {}

        def __del__(self):
                print('Destructor called, Point cloud deleted.')
                del self

        def setColorPointCloud(self, colorImage):
                self.colorImage = colorImage

        def setVertex(self, vertex):
                self.vertex = vertex
                self.pointCloud['vertex'] = self.vertex

        def setConfigration(self, filterKn, neighbors,
                filterClean, ValueCleanPoint, radioPointCloud):
                """
                docstring
                """
                self.filterKn = filterKn
                self.Nneighbors = neighbors
                self.filterClean = filterClean
                self.ValueCleanPoint = ValueCleanPoint
                self.radioPoint = radioPointCloud
                
        def NPoints(self):
                """
                docstring
                """
                return self.N

        def getPointCloudWidget(self):
                if self.filterClean:
                        print('cleaning points...')
                        vertex = Points(self.vertex, r = self.radioPoint).clean(self.ValueCleanPoint)
                else:
                        vertex = Points(self.vertex, r = self.radioPoint)

                if self.filterKn:
                        print('adding filterKn...')
                        self.pointCloudKN = []
                        self.knNeighbors(vertex.points(), 1)
                        vertex = Points(self.pointCloudKN[-1], r = self.radioPoint)

                scalars = vertex.points()[:, 2]
                vertex.pointColors(scalars, cmap="coolwarm")
                #vertex.pointColors(scalars, cmap="binary")
                self.N = vertex.N()

                self.pointCloud['vertex'] = vertex.points()
                self.pointCloud['color'] = np.array([[0,0,0]])
                self.pointCloudVedo = vertex
                widgetPointCloud = self.getRenderPointCloud(vertex)
                return widgetPointCloud

        def getColorPointCloudWidget(self):
                if self.filterClean:
                        print('cleaning points...')
                        vertex = Points(self.vertex, r = self.radioPoint).clean(self.ValueCleanPoint)
                else:
                        vertex = Points(self.vertex, r = self.radioPoint)

                if self.filterKn:
                        print('adding filterKn...')
                        self.pointCloudKN = []
                        self.knNeighbors(vertex.points(), 1)
                        rgb, newXYZ = self.transformation.getColorFromXYZ(
                            np.array(self.pointCloudKN[-1]), self.colorImage)
                else:
                        rgb, newXYZ = self.transformation.getColorFromXYZ(
                            vertex.points(), self.colorImage)

                #self.planeSegmentation(vertex.points())
                print('adding color...')
                vertex = Points(newXYZ, r = self.radioPoint, c = rgb)
                #plt = Plotter()
                #plt.show(vertex, viewup="z", interactive=True )
                self.N = vertex.N()
                self.pointCloud['vertex'] = vertex.points()
                self.pointCloud['color'] = rgb
                self.pointCloudVedo = vertex
                widgetPointCloud = self.getRenderPointCloud(vertex)
                return widgetPointCloud

        def getRenderPointCloud(self, actor):
                renderer = vtk.vtkRenderer()
                renderer.AddActor(actor)
                #renderer.SetBackground(1 / 255, 20 / 255, 30 / 255)
                renderer.SetBackground(33 / 255, 33 / 255, 33 / 255)
                renderer.ResetCamera()

                self.widgetPointCloud = QVTKRenderWindowInteractor()
                self.widgetPointCloud.Initialize()
                self.widgetPointCloud.Start()

                self.widgetPointCloud.GetRenderWindow().AddRenderer(renderer)

                #return renderer
                return self.widgetPointCloud

        def closeWindow(self):
                render_window = self.widgetPointCloud.GetRenderWindow()
                render_window.Finalize()
                #self.widgetPointCloud.TerminateApp()
                #del render_window, self.widgetPointCloud

        def getPointCloud(self):
                """
                docstring
                """
                return {
                        'vertex': self.pointCloud['vertex'].tolist(),
                        'color': self.pointCloud['color'].tolist()
                }

        def getPointCloudVedo(self):
                """
                docstring
                """
                return self.pointCloudVedo

        def toMesh(self, coords):
                print("point cloud to mesh")
                d0 = Points(coords, r=2, c="b").legend("source")
                d1 = delaunay2D(coords, mode='fit')
                d1.color("r").wireframe(True).legend("delaunay mesh")
                #cents = d1.cellCenters()
                #ap = Points(cents).legend("cell centers")
                # NB: d0 and d1 are slightly different
                show(d0, d1, __doc__, at=0)
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
                reco = recoSurface(pts1, dims=200, radius=0.01).legend(
                    "surf. reco")
                vp.show(reco, at=2, axes=7, zoom=1.2, interactive=1)

        def knNeighbors(self, vertices, nIteration):
                print(len(vertices))
                vertices = Points(vertices)#.clean(0.002)
                #vertices = Points(vertices)
                nIteration = nIteration-1
                if nIteration >= 0:
                        print(nIteration)
                        newPointCloud = []
                        for i in range(vertices.N()):
                                pt = vertices.points()[i]
                                ids = vertices.closestPoint(
                                    pt, N = self.Nneighbors, returnIds = True)
                                newPointCloud.append(
                                    np.mean(vertices.points()[ids], axis = 0).tolist())
                        newPointCloud = np.array(newPointCloud)
                        self.pointCloudKN.append(newPointCloud)
                        self.knNeighbors(newPointCloud, nIteration)

        def centerPlane(self, vertices, nIteration):
                nIteration = nIteration-1
                vertices = Points(vertices)  # .clean(tol=0.0001)
                if nIteration >= 0:
                        print(nIteration)
                        points = []
                        for i, p in enumerate(vertices.points()):
                                pts = vertices.closestPoint(p, N=10)
                                # find the fitting plane
                                plane = fitPlane(pts)
                                points.append(plane.center)
                        points = np.array(points)
                        self.centerPlane(points, nIteration)
                        return points

        def clusterPointCloud(self, xyzPoints):
                points = Points(xyzPoints)
                clusterPoint = cluster(xyzPoints, radius=0.055)
                print(clusterPoint)
                print(clusterPoint.info.keys())
                print(len(clusterPoint.info['clusters']))
                newPoints = clusterPoint.info['clusters'][0]
                newPoints = Points(newPoints)

                show(newPoints,   __doc__, viewup='z')
                return clusterPoint

        def planeSegmentation(self, xyzPoints):
                auxPoints = Points(xyzPoints)
                points = Points(xyzPoints[::2,:]).clean(0.005)
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
                show(points, plane, arrows, __doc__, viewup='z')
