import urlfetch
import json


def insertClient(id, name, lastname, empresa, phone, email):
    response = urlfetch.post(
        'http://localhost:3000/cliente/addcliente',
        headers={},
        data={
            "id": id, 
            "name": name,
            "lastname": lastname,
            "empresa": empresa,
            "phone": phone,
            "email": email
        },
    )
    res = json.load(response)
    return res['status']
