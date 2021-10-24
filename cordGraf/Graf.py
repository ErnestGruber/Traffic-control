import matplotlib.pyplot as plt
import pandas as pd
from POST.GET import GetAll
import xlwt

table = pd.read_excel('/Users/valerijkutuzov/PycharmProjects/Traffic-control/RawData/GradData.xlsx')

class GradCreate():
    def Grad(num1, num2):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('GradData', cell_overwrite_ok=True)
        ws.write(0, 0, 'Routes')
        ws.write(0, 1, 'Green')
        ws.write(0, 2, 'Yellow')
        ws.write(0, 3, 'Red')
        for y in range(1, 10):
            for o in (1950, 1800, 1600, 1400, 1150, 950, 800, 550, 300):
                print(o)
                ws.write(y, 0, o)
        for i in range(num1, num2):
            for l in range (0,2):
                for b in range(1,4):
                    for c in range(1,11):
                        t_osn = GetAll.Get(i)['phases'][l]['t_osn']
                        t_prom = GetAll.Get(i)['phases'][l]['t_prom']
                        t_min = GetAll.Get(i)['phases'][l]['t_min']
                        greenlen = t_osn + t_min
                        yellowlwn = t_prom
                        reslen = t_osn
                        ws.write(b, c, greenlen)
                        ws.write(b + 1, c+1, yellowlwn)
                        ws.write(b + 2, c+2, reslen)
        wb.save('/Users/valerijkutuzov/PycharmProjects/Traffic-control/RawData/GradColl')

GradCreate.Grad(71030, 71040)
table.plot.barh('Road', stacked=True)

plt.show()





