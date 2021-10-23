from LRUcache import LRUcache
class cache(LRUcache):
    def go_to_bin_file (self):
        def coding(sq:str):
            res=''
            dict={'a':'01000001','b':'01000010','c':'01000011','d':'01000100','e':'01000101','f':'01000110','g':'01000111','h':'01001000','i':'01001001','j':'01001010','k':'01001011','l':'01001100','m':'01001101','o':'01001111','q':'01010001','r':'01010010','s':'01010011','t':'01010100','u':'01010101','v':'01010110','w':'01010111','x':'01011000','y':'01011001','z':'01011010','n':'01001110','p':'01010000','0':'00110000','1':'00110001','2':'00110010','3':'00110011','4':'00110100','5':'00110101','6':'00110110','7':'00110111','8':'00111000','9':'00111001',}
            for i in sq:
                res+=dict.get[i]
            return res

        F=open(self.file_output,'w')
        for key, value in dict.items():
            F.write(key)
            F.write(' ')
            F.write(value)
            F.write('\n')
        F.close()
        self.dict=None
    def go_to_cache (self):
        F=open(self.file_output)
        data=LRUcache(50)
        for i in range(data.size):
            line = F.readline().split()
            if not line:
                break
            else:
                key=line[0]
                value=line[1]
                data.put(key,value)

dict={'ladno':'net','da':'gg'}
cesh=cache(2,dict,'bin_test_data')
cesh.go_to_bin_file()
F=open('bin_test_data.txt','w')
F.write('5')
F.close()