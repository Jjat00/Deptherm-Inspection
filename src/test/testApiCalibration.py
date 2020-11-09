import base64
import cv2
import urlfetch
import json


def insertCalibration(id, idUsuario, idTipoCalib, paramFocales, paramDistortion, matrizHomografia):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addCalibration',
        headers = {},
        data = {
            'id': id,
            'idUsuario': idUsuario,
            'idTipoCalib': idTipoCalib,
            'paramFocales': paramFocales,
            'paramDistortion': paramDistortion, 
            'matrizHomografia': matrizHomografia            
        },
    )
    res = json.load(response)
    print(res)

def getCalibration(id):
    """
    docstring
    """

    res = urlfetch.get(
        'http://localhost:3000/calibracion/getCalib/%i'%id)
    r = res.content.decode('utf-8')
    u = json.loads(r)
    print(u[0]['matrizhomografia']['matriz'])


#getCalibration(3)

#insertCalibration(3, 1144000000, 1, 
#    """{
#        "Fy": 686.721003,
#        "Fx": 684.485947,
#        "Cx": 287.337264,
#        "Cy": 262.611702}
#    """,
#    """{
#        "K1": -0.232876,
#        "K2": 1.292407,
#        "K3": -3.291786,
#        "p1": -0.002949,
#        "p2": -0.004483
#    }
#    """,
#    """{
#        "matriz": [[570.5725384259518, 0.0, 335.17270110938176],
#                   [0.0, 570.5544526637268, 246.2629901893306],
#                   [0.0, 0.0, 1.0]]
#    }""")


def insertImage(name, idCalibration, image):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addImageCalib',
        headers={},
        data={
            'name': name,
            'idCalibracion': idCalibration,
            'imagen': image
        },
    )
    res = json.load(response)
    return res['status']

image = cv2.imread('test/depthImage.png')
buffer = cv2.imencode('.jpg', image)[1]
jpg_as_text = base64.b64encode(buffer)


insertImage('imagen3', 4, jpg_as_text)


#print('jpg_as_text')
#print(jpg_as_text)

jpg_original = base64.b64decode(jpg_as_text)

import numpy as np

jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
image_buffer = cv2.imdecode(jpg_as_np, flags=1)

cv2.imshow('img', image_buffer)
cv2.waitKey(200)


def getImage():
    res = urlfetch.get('http://localhost:3000/calibracion/getImage/4')
    r = res.content.decode('utf-8')
    u = json.loads(r)
    imagen = u[5]['imagen']['data']
    return imagen


#imagen = getImage()
#arr = bytes(imagen)

#newImage = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

