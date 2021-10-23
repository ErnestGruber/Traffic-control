import json
import requests


class SendGet:
        @classmethod
        def full_info(self,id):
            response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info')
            data=response.json()
            return data

        @classmethod
        def status(self,id):
            response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/status')
            return response.json()

        @classmethod
        def get_id_command(self,id):
            data=self.status(id)
            current_program_id=data["current_program_id"]
            return current_program_id

a=SendGet()
data=a.full_info(71031)
print(data)