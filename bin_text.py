import os
class bin_data:
    def __init__(self,file_input,file_output):
        self.file_input=file_input
        self.file_output=file_output

    def go_to_bin (self):
        def binary(n):
            b = ''
            while n > 0:
                b = str(n % 2) + b
                n = n // 2
            return b
        Fin_1 = open(self.file_input)
        Fin_2 = open(self.file_output, 'w')
        while True:
            line=Fin_1.readline()
            if not line:
                break
            for i in line.split():
                Fin_2.write(binary(int(i)))
                Fin_2.write(' ')
            Fin_2.write('\n')

        Fin_2.close()
        Fin_1.close()
        if os.path.isfile(self.file_input):
            os.remove(self.file_input)
        else:
            print('Error')

class ten_data:
    def __init__(self,file_input,file_output):
        self.file_input=file_input
        self.file_output=file_output

    def go_to_ten (self):
        def ten(data):
            number = 0
            len_dat = len(data)
            for i in range(0, len_dat):
                number += int(data[i]) * (2**(len_dat - i -1))
            return str(number)
        Fin_1 = open(self.file_input)
        Fin_2 = open(self.file_output, 'w')
        while True:
            line=Fin_1.readline()
            if not line:
                break
            for i in line.split():
                Fin_2.write(ten(i))
                Fin_2.write(' ')
            Fin_2.write('\n')

        Fin_2.close()

