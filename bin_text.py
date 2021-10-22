def binary(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
def ten(data):
    number = 0
    len_dat = len(data)
    for i in range(0, len_dat):
        number += int(data[i]) * (2**(len_dat - i -1))
    return str(number)

def go_to_bin (file_input:str, file_output:str):
    Fin_1 = open(file_input)
    Fin_2 = open(file_output, 'w')
    while True:
        line=Fin_1.readline()
        if not line:
            break
        for i in line.split():
            Fin_2.write(binary(int(i)))
            Fin_2.write(' ')
        Fin_2.write('\n')

    Fin_2.close()


def go_to_ten (file_input:str, file_output:str):
    Fin_1 = open(file_input)
    Fin_2 = open(file_output, 'w')
    while True:
        line=Fin_1.readline()
        if not line:
            break
        for i in line.split():
            Fin_2.write(ten(i))
            Fin_2.write(' ')
        Fin_2.write('\n')

    Fin_2.close()


