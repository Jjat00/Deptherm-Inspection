import urlfetch
import json


def insertPointCloud(idnube, vertex, color):
    response = urlfetch.post(
        'http://localhost:3000/nubepuntos/addnubepuntos',
        headers={},
        data={
            'idnube': idnube,
            'vertices': vertex,
            'color': color
        },
    )
    res = json.load(response)
    return res['status']


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
