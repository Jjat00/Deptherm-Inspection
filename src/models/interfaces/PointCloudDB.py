import urlfetch
import json


def insertPointCloud(vertex, color):
    response = urlfetch.post(
        'http://localhost:3000/nubepuntos/addnubepuntos',
        headers={},
        data={
            'vertices': vertex,
            'color': color
        },
    )
    res = json.load(response)
    return res['status']


def getLastPointCloud():
    res = urlfetch.get(
        'http://localhost:3000/nubepuntos/last')
    r = res.content.decode('utf-8')
    u = json.loads(r)
    id = u[0]['idnube']
    return id

def insertImagesCloud(idnube, rgbImage, depthImage, thermalImage, colorImage):
    response = urlfetch.post(
        'http://localhost:3000/nubepuntos/addimagenesnube',
        headers={},
        data={
            'idnube': idnube,
            'imagenRgb': rgbImage,
            'imagenProfundidad': depthImage,
            'imagenTermica': thermalImage,
            'imagenFalsoColor': colorImage
        },
    )
    res = json.load(response)
    return res['status']
