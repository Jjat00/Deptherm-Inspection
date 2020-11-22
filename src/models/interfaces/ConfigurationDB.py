import urlfetch
import json


def insertConfig(name, place, emissivity, tem_amb, order):
    response = urlfetch.post(
        'http://localhost:3000/configuracion/addConfig',
        headers={},
        data={
            'nombre': name,
            'lugar': place,
            'emisividad': emissivity,
            'tem_amb': tem_amb,
            'pedido': order

        },
    )
    res = json.load(response)
    return res['status']
