import requests
import json
from GET import SendGet


class SendPost:
    keep_id_controller = []
    keep_id_phase={}
    def create_key_in_dict(self,id_controller):
        SendPost.keep_id_phase[id_controller]=[]
    def check_in_dict_second(self, id_controller):
        SendPost.keep_id_phase = list(set(SendPost.keep_id_phase))  # роверяем значения в словаре
        if id_controller in SendPost.keep_id_phase:
            return 1
        else:
            return 0

    @classmethod
    def check_in_dict_first(self, id_controller):
        SendPost.keep_id_phase=list(set(SendPost.keep_id_phase))    # роверяем значения в словаре
        if id_controller in SendPost.keep_id_phase:
            return 1
        else:
            return 0

    @classmethod
    def custom_phase_program(cls, id_controller, config_phase):  # передаем значение в виде словаря time =
        t_cycle = 0  # {0: [3,1632402791], 1: [31, 9, 4], 2: [13, 9, 4]}
        phases = []
        for item in range(len(config_phase) - 1):
            data_phases = config_phase[item + 1]
            t_cycle = data_phases[0] + data_phases[1] + t_cycle
            phases.append({"id": item + 1,
                           "t_osn": data_phases[0],
                           "t_prom": data_phases[1],
                           "t_min": data_phases[2],
                           "is_hidden": False,    # можно установить значение из словаря но мы не имеем к нему доступ
                           "directions": False})  # можно установить значение из словаря но мы не имеем к нему доступ
        data = {"start_phase_id": config_phase[0][0],
                "time_start_sync": config_phase[0][1],
                "t_cycle": t_cycle,
                "phases": phases}
        print(data)
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id_controller}/custom_phase_program', json=data)
        data=json.loads(response.text)
        if SendPost.check_in_dict_first(id_controller)==1:
            SendPost.keep_id_phase.update({id_controller:[SendGet.status(id_controller),SendGet.get_id_command(id_controller)]})
        else:
            SendPost.create_key_in_dict({id_controller:[SendGet.status(id_controller),SendGet.get_id_command(id_controller)]})
        return response

    @classmethod
    def set_fix_program(cls, id_controller, deadline, force):
        if id_controller in SendPost.keep_id_phase == 0:
            return "WRONG"
        else:
            id_command = SendGet.get_id_command(id_controller)
            response = requests.post(
                f'https://api.via-dolorosa.ru/rc/{id_controller}/set_fix_program/{id_command}'
                f'?deadline={deadline}&force={force}')
            return response

    @classmethod
    def send_program(cls, id_controller):
        if cls.chek_phase(id_controller) == 2:
            return "WRONG"
        else:
            response = requests.post(f'https://api.via-dolorosa.ru/rc/{id_controller}/send_program')
            return response

    @classmethod
    def set_local(cls, id_controller):
        if cls.chek_phase(id_controller) == 2:
            return "WRONG"
        else:
            response = requests.post(f'https://api.via-dolorosa.ru/rc/{id_controller}/set_local')
            return response

    @classmethod
    def continue_current_phase(cls, id_controller, time_to_continue):
        if cls.chek_phase(id_controller) == 2:
            return "WRONG"
        else:
            response = requests.post(
                f'https://api.via-dolorosa.ru/rc/{id}/continue_current_phase?phase_id='
                f'{SendGet.get_id_phase(id_controller)}&timeout={time_to_continue}')
            return response

    @classmethod
    def forward_next_phase(cls, id_controller):
        if cls.chek_phase(id_controller) == 2:
            return "WRONG"  # in process
        else:
            response = requests.post(f'https://api.via-dolorosa.ru/rc/{id_controller}/forward_next_phase')
            return response

    @classmethod
    def keep_phase(cls, id_controller):
        if cls.chek_phase(id_controller) == 2 or SendPost.keep_id_controller.index(id_controller):
            return "WRONG"  # in process
        else:
            SendPost.keep_id_controller.append(id_controller)
            response = requests.post(
                f'https://api.via-dolorosa.ru/rc/{id}/keep_phase/{SendGet.get_id_phase(id_controller)}')
            return response

    @classmethod
    def cancel_keep_phase(cls, id_controller):
        if SendPost.keep_id_controller.index(id_controller):
            response = requests.post(
                f'https://api.via-dolorosa.ru/rc/{id}/keep_phase/{SendGet.get_id_phase(id_controller)}')
            SendPost.keep_id_controller.remove(id_controller)
            return response
        else:
            return "WRONG"  # in process


time = {0: [3, 1632402791], 1: [31, 9, 4], 2: [13, 9, 4], 3: [25, 9, 15]}
a = SendPost()
a.custom_phase_program(71037,time)
a.set_fix_program(71037,60,"false")