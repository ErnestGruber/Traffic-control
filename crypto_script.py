import requests
def coding(sq: str):
    sq=str(sq)
    res = ''
    dict = {'a': '01000001', 'b': '01000010', 'c': '01000011', 'd': '01000100', 'e': '01000101', 'f': '01000110',
            'g': '01000111', 'h': '01001000', 'i': '01001001', 'j': '01001010', 'k': '01001011', 'l': '01001100',
            'm': '01001101', 'o': '01001111', 'q': '01010001', 'r': '01010010', 's': '01010011', 't': '01010100',
            'u': '01010101', 'v': '01010110', 'w': '01010111', 'x': '01011000', 'y': '01011001', 'z': '01011010',
            'n': '01001110', 'p': '01010000', '0': '00110000', '1': '00110001', '2': '00110010', '3': '00110011',
            '4': '00110100', '5': '00110101', '6': '00110110', '7': '00110111', '8': '00111000', '9': '00111001','_':'01011111',
            'A': '01100001','B': '01100010','C':'01100011','D':'01100100','E':'01100101','F':'01100110','G':'01100111','H':'01101000',
            'I':'01101001','J':'01101010','K':'01101011','L':'01101100','M':'01101101','O':'01101111','Q':'01110001','R':'01110010',
            'S':'01110011','T':'01110100','U':'01110101','V':'01110110','W':'01110111','X':'01111000','Y':'01111001','Z':'01111010',
            'N':'01101110','P':'01110000',' ':'11100000',':':'00111010','.':'01100000','-':'11000000'}
    for i in sq:
        res += dict.get(i)
    return res


def full_info(num):
    response = requests.get(f'https://api.via-dolorosa.ru/rc/{num}/full_info')
    json_dict = response.json()
    return json_dict


def crypto(data):
    B = [{}, {}, {}]
    new_data = {}
    temp_data = {}
    for i in data:
        if i == 'phases':
            new_data[i] = data[i]
    data.pop('phases')
    l = new_data['phases']
    count = 0
    for i in l:
        for j in i:
            key = j
            value = i[j]
            B[count][coding(key)] = coding(value)
        count += 1
    temp_data[coding("phases")] = B

    for i in data:
        key = i
        value = data[i]
        temp_data[coding(key)] = coding(value)
    return temp_data
#data = full_info(71031)

data={
  "time": 1634747720,
  "id": 1,
  "rc_created_at": "2021-10-20T12:22:58.35137Z",
  "rc_updated_at": "2021-10-20T16:35:19.545886Z",
  "num_tl": 3228,
  "name": "Танковый пр-д Краснокурсантский 1 пр-д ",
  "is_enabled": 'true',
  "is_alarmed": 'true',
  "type": "SYNTEZ",
  "protocol": "SCTIP",
  "conn_status": "OK",
  "mode": "CC_CALENDAR",
  "program_id": 7,
  "keep_phase_id": 0,
  "changed_time_at": "2021-10-20T14:00:01.27971Z",
  "real_mode": "LOCAL",
  "real_program_id": 7,
  "real_keep_phase_id": 0,
  "program_created_at": "2021-10-20T12:22:58.349945Z",
  "program_updated_at": "2021-10-20T12:22:58.349945Z",
  "t_cycle": 90,
  "program_type": "LOCAL",
  "phases": [
    {
      "id": 1,
      "t_osn": 32,
      "t_prom": 6,
      "t_min": 4,
      "is_hidden": 'false',
      "directions": [
        1,
        2
      ]
    },
    {
      "id": 2,
      "t_osn": 25,
      "t_prom": 6,
      "t_min": 4,
      "is_hidden": 'false',
      "directions": [
        3
      ]
    },
    {
      "id": 3,
      "t_osn": 15,
      "t_prom": 6,
      "t_min": 15,
      "is_hidden": 'false',
      "directions": [
        4,
        5,
        6
      ]
    }
  ],
  "start_phase_id": 1

}




temp_data=crypto(data)
def file(data):
    data=temp_data
    data_hard=data.pop('010100000100100001000001010100110100010101010011')
    print(data)
    F=open('cache_file','w')
    for i in data:
        key=i
        value=data[key]
        F.write(key)
        F.write(' ')
        F.write(value)
        F.write('\n')
    print(data_hard)
    for i in data_hard:
        for j in i:
            key = j
            value = i[j]
            F.write(key)
            F.write(' ')
            F.write(value)
            F.write('\n')
    F.close()
file(data)





