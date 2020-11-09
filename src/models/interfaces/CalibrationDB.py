import urlfetch
import json


def insertCalibration(id, idUsuario, idTipoCalib, paramFocales, paramDistortion, matrizHomografia):
    response = urlfetch.post(
        'http://localhost:3000/calibracion/addCalibration',
        headers={},
        data={
            'id': id,
            'idUsuario': idUsuario,
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
