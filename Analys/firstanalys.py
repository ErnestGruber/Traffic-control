import pandas as pd
from scipy import cluster
from scipy.cluster.vq import kmeans
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np

class AnomalyFind(ABC):
    @abstractmethod
    def find(data, param):
        dataFPO = pd.read_excel(f'{data}')
        dataFPO.head()
        intensive_raw = dataFPO[f'{param}'].values
        intensive_raw = intensive_raw.reshape(-1, 1)
        intensive_raw = intensive_raw.astype('float64')
        centroids, avg_distance = kmeans(intensive_raw, 4)
        groups, cdist = cluster.vq.vq(intensive_raw, centroids)
        plt.scatter(intensive_raw, np.arange(0, len(intensive_raw), 1), c=groups)
        plt.xlabel(f'{param}')
        plt.ylabel('Values')
        plt.show()
        error = intensive_raw.max()
        print(error)

test = AnomalyFind.find('/Users/valerijkutuzov/Downloads/Пример данных с детекторов транспорта /rawdata/ДТ1_От_ул_Фёдора_Полетаева_к_Окскому_пр_ду.xls', 'Intensive')

print(test)




