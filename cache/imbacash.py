from cache.LRUcache import LRUcache
from cache.crypto_script import F
import requests
def full_info(num):
    response = requests.get(f'https://api.via-dolorosa.ru/rc/{num}/full_info')
    json_dict = response.json()
    return json_dict

def encoding(sq):
    dict = {'01000001': 'a', '01000010': 'b', '01000011': 'c', '01000100': 'd', '01000101': 'e', '01000110': 'f',
            '01000111': 'g', '01001000': 'h', '01001001': 'i', '01001010': 'j', '01001011': 'k', '01001100': 'l',
            '01001101': 'm', '01001111': 'o', '01010001': 'q', '01010010': 'r', '01010011': 's', '01010100': 't',
            '01010101': 'u', '01010110': 'v', '01010111': 'w', '01011000': 'x', '01011001': 'y', '01011010': 'z',
            '01001110': 'n', '01010000': 'p', '00110000': '0', '00110001': '1', '00110010': '2', '00110011': '3',
            '00110100': '4', '00110101': '5', '00110110': '6', '00110111': '7', '00111000': '8', '00111001': '9',
             '01011111':'_',
            '01100001': 'A','01100010': 'B','01100011':'C','01100100':'D','01100101':'E','01100110':'F','01100111':'G','01101000':'H',
            '01101001':'I','01101010':'J','01101011':'K','01101100':'L','01101101':'M','01101111':'O','01110001':'Q','01110010':'R',
            '01110011':'S','01110100':'T','01110101':'U','01110110':'V','01110111':'W','01111000':'X','01111001':'Y','01111010':'Z',
            '01101110':'N','01110000':'P','11100000':' ','00111010':':','01100000':'.','11000000':'-'}
    res = ''
    sq=str(sq)
    sq_new = ''
    for i in sq:
        if len(sq_new) != 8:
            sq_new += i
        else:
            res += dict[sq_new]
            sq_new = ''
            sq_new += i
    res += dict[sq_new]
    return res
temp_data = full_info(71031)
q=temp_data['phases']

def imbacash():
    data=LRUcache(50)
  #  path="C:/Users/timur/PycharmProjects/Traffic-control/cache/cache_file"
    F=open("C:/Users/timur/PycharmProjects/Traffic-control/cache/cache_file")
    while True:
        line=F.readline().split()
        if not line:
            break
        else:
            data.put(encoding(line[0]),encoding(line[1]))
    data.put('phases',q)

    return data



