class bin_file:
    def __init__(self,dict,file_output):
        self.dict=dict
        self.file_output=file_output

    def go_to_bin_file(self):
        def coding(sq:str):
            res=''
            sq=str(sq)
            dict={'a':'01000001','b':'01000010','c':'01000011','d':'01000100','e':'01000101','f':'01000110','g':'01000111','h':'01001000','i':'01001001','j':'01001010','k':'01001011','l':'01001100','m':'01001101','o':'01001111','q':'01010001','r':'01010010','s':'01010011','t':'01010100','u':'01010101','v':'01010110','w':'01010111','x':'01011000','y':'01011001','z':'01011010','n':'01001110','p':'01010000','0':'00110000','1':'00110001','2':'00110010','3':'00110011','4':'00110100','5':'00110101','6':'00110110','7':'00110111','8':'00111000','9':'00111001',}
            for i in sq:
                res+=dict.get(i)
            return res
        F=open(self.file_output,'w')
        for key, value in dict.items():
            key_new=coding(key)
            value_new=coding(value)
            F.write(key_new)
            F.write(' ')
            F.write(value_new)
            F.write('\n')
        F.close()
        self.dict=None

class bin_dict:
    def __init__(self,file_output):
        self.dict={}
        self.file_output=file_output

    def go_to_bin_dict(self):
        F=open(self.file_output)
        while True:
            line=F.readline().split()
            if not line:
                break
            else:
                key=line[0]
                value=line[1]
                self.dict[key]=value
        return self.dict


class json_dict:
    def __init__(self,dict):
        self.dict = dict
        self.new_dict = {}

    def go_to_json_dict(self):
        def encoding(sq:str):
            dict={'01000001':'a','01000010':'b','01000011':'c','01000100':'d','01000101':'e','01000110':'f','01000111':'g','01001000':'h','01001001':'i','01001010':'j','01001011':'k','01001100':'l','01001101':'m','01001111':'o','01010001':'q','01010010':'r','01010011':'s','01010100':'t','01010101':'u','01010110':'v','01010111':'w','01011000':'x','01011001':'y','01011010':'z','01001110':'n','01010000':'p','00110000':'0','00110001':'1','00110010':'2','00110011':'3','00110100':'4','00110101':'5','00110110':'6','00110111':'7','00111000':'8','00111001':'9','11111111':'_'}
            res=''
            sq_new=''
            for i in sq:
                if len(sq_new)!=8:
                    sq_new+=i
                else:
                    res+=dict[sq_new]
                    sq_new=''
                    sq_new+=i
            res+=dict[sq_new]
            return res
        for j in self.dict:
            key,value=j,self.dict[j]
            self.new_dict[encoding(key)]=encoding(value)
        return self.new_dict






