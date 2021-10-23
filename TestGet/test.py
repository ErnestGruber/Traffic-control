import requests


def Get(id):
    response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info', data={'key':'value'})
    return response

data = Get(71031)

print(data.json())