import pandas as pd
from scipy import cluster
from scipy.cluster.vq import kmeans
from abc import ABC, abstractmethod

class AnomalyFind(ABC):
    @abstractmethod
    def find(self, data, param):
        dataFPO = pd.read_excel(f'{data}')
        dataFPO.head()
        intensive_raw = dataFPO[f'{param}'].values
        intensive_raw = intensive_raw.reshape(-1, 1)
        intensive_raw = intensive_raw.astype('float64')
        centroids, avg_distance = kmeans(intensive_raw, 4)
        groups, cdist = cluster.vq.vq(intensive_raw, centroids)
        error = cdist.max()
        print(error)





