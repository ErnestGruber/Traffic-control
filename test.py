import requests
import json


with open("body.json", "r") as read_file:
    data = json.load(read_file)
    print(type(data))
def Post(id):
    responce = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/custom_phase_program', json=data )
    print(responce.text)
    return responce
Post(71031)
