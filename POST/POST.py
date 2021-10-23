import requests
from GET import SendGet


class SendPost:
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
                           "is_hidden": False,  # можно установить значение из словаря но мы не имеем к нему доступ
                           "directions": False})  # можно установить значение из словаря но мы не имеем к нему доступ
        data = {"start_phase_id": config_phase[0][0],
                "time_start_sync": config_phase[0][1],
                "t_cycle": t_cycle,
                "phases": phases}
        print(data)
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id_controller}/custom_phase_program', json=data)
        return response

    @classmethod
    def chek_phase(self, id):
        response = requests.get(f'https://api.via-dolorosa.ru/rc/{id}/full_info')
        json_dict = response.json()
        if json_dict["phases"] is None:
            return 2
        else:
            return 1

    def set_fix_program(self, id):
        if self.chek_phase(id) == 2:
            return "WRONG"  # in process
        else:
            id_command = SendGet.get_id_command(id)
            response = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/set_fix_program/{id_command}?deadline=60&force=false')
            print(response.text, 3333)

    def send_program(self, id):
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/send_program')
        print(response.text)  # in process
        return response


time = {0: [3, 1632402791], 1: [31, 9, 4], 2: [13, 9, 4], 3: [25, 9, 15]}
a = SendPost()
a.set_fix_program(71032)
