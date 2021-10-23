import json
import requests


class SendGet:
        @classmethod
        def full_info(cls, id):
            return json.loads(requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info').text)

        @classmethod
        def status(cls, id):
            return json.loads(requests.get(f'https://api.via-dolorosa.ru/rc/{id}/status').text)

        @classmethod
        def get_id_command(cls, id):
            return cls.status(id)["current_program_id"]   #current_program_id
        @classmethod
        def get_id_phase(cls, id ):
            return cls.status(id)["current_phase_id"]     #
