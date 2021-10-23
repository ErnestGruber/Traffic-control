import requests


class GetAll():
    def Get(id):
        response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info')
        return response.json()


class GetCurrentStatus():
    def Get(id):
        response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/status')
        return response.json()

class PostCustomPhase():
    def Post(id, body):
        responce = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/custom_phase_program', json=body)
        return responce.json()

class TakePhase:
    def Post(id):
        responce = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/forward_next_phase')
        return responce
