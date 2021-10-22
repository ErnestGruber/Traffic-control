from pandas import read_csv, DataFrame, Series


dataFPO = read_csv('RawData/FedorsPoletarva-Okskomy.csv', sep=';', comment='#')
dataSFP = read_csv('RawData/Shumilovo-FedoraPoletaeva.csv')
dataVS = read_csv('RawData/Volgogradskiy-Shumilovo.csv')
dataZelZG = read_csv('RawData/Zelenodoliskaya-Zgigulevskoe.csv')
dataZgZel = read_csv('RawData/Zgigulevskoe-Zelenodoliskaya.csv')

dataFPO.pivot_table('Time', 'Intensive', 'MotoUnit', 'count').plot(kind='bar', stacked=True)
