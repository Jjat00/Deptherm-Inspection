from vedo import *

pointCloud = load('test/imagesPointCloud.ply')

normal = pointCloud.computeNormalsWithPCA()

points = pointCloud.points()
print(points[:1000,:])
pointsNormal = normal.points()
color = pointCloud.c()
print(points)
print(pointsNormal)

clusterPoint = cluster(points, radius=0.02)
print(clusterPoint)
print(clusterPoint.info.keys())
print(len(clusterPoint.info['clusters']))
newPoints = clusterPoint.info['clusters'][0]
newPoints = Points(newPoints)
#print(clusterPoint.info['clusters'])
show(newPoints, __doc__, axes=1, viewup='z')
#show(clusterPoint, __doc__, axes=1, viewup='z')

