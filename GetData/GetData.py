import requests
def Get(id):
    response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info') ## полная инфа
    return response

class GetCurrentStatus():
    def Get(self,request, id):
        response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/status') ##
        return response

class PostCustomPhase():
    def Post(self, request, id, body):
        responce = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/custom_phase_program', json=body) ##
        return responce