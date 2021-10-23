import requests
class Send_Post:
    @classmethod
    def custom_phase_program(self, id, time): ## передаем значение в виде словаря time =
        t_cycle = 0                            # {0: [3,1632402791], 1: [31, 9, 4, False, None], 2: [13, 9, 4, False, None], 3: [25, 9, 15, False, None]}
        phases = []
        for item in  range(len(time)-1):
            data_phases = time[item+1]
            t_cycle=data_phases[0]+data_phases[1]+t_cycle
            phases.append({"id": item + 1,
                           "t_osn": data_phases[0],
                           "t_prom": data_phases[1],
                           "t_min": data_phases[2],
                           "is_hidden": data_phases[3],
                           "directions": data_phases[4]})
        data = {"start_phase_id": time[0][0],
                "time_start_sync": time[0][1],
                "t_cycle": t_cycle,
                "phases": phases}
        print(data)
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/custom_phase_program', json=data)
        print(response.text)
        return response

    def set_fix_program(self,id):
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/set_fix_program/1?deadline=60&force=false')
        print(response.text)
        return response

    def send_program(self,id):
        response = requests.post(f'https://api.via-dolorosa.ru/rc/{id}/send_program')
        print(response.text)
        return response

time = {0: [3,1632402791], 1: [31, 9, 4, False, None], 2: [13, 9, 4, False, None], 3: [25, 9, 15, False, None]}
a=Send_Post()
a.set_fix_program(71032)