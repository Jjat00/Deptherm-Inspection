import urlfetch
import json


def insertCalibration(camera, idUsuario, idTipoCalib, paramFocales, paramDistortion, matrizHomografia):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addCalibration',
        headers={},
        data={
            'idUsuario': idUsuario,
            'camara': camera,
            'idTipoCalib': idTipoCalib,
            'paramFocales': paramFocales,
            'paramDistortion': paramDistortion,
            'matrizHomografia': matrizHomografia
        },
    )
    res = json.load(response)
    return res['status']


def getCalibration(id):
    res = urlfetch.get(
        'http://localhost:3000/calibracion/getCalib/%i' % id)
    r = res.content.decode('utf-8')
    u = json.loads(r)
    print(u[0]['matrizhomografia']['matriz'])


def insertImage( idCalibration, image):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addImageIntrCalib',
        headers={},
        data={
            'idCalibracion': idCalibration,
            'imagen': image
        },
    )
    res = json.load(response)
    return res['status']

def insertImages( idCalibration, imageSrc, imageDst):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addImageExtrCalib',
        headers={},
        data={
            'idCalibracion': idCalibration,
            'imagen_src': imageSrc,
            'imagen_dst': imageDst
        },
    )
    res = json.load(response)
    return res['status']


def getLastCalib():
    res = urlfetch.get(
        'http://localhost:3000/calibracion/getLastCalib')
    r = res.content.decode('utf-8')
    u = json.loads(r)
    print(u)
    print(u[0]['id'])
    id = u[0]['id']
    return id
