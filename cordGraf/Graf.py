import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
from GetData import GetAll

print(GetAll.Get(71031))

t_osn = GetAll.Get(71031)['phases'][2]['t_osn']
t_prom = GetAll.Get(71031)['phases'][2]['t_prom']
t_min = GetAll.Get(71031)['phases'][2]['t_min']

print(t_osn+t_min)
print(t_prom)
print(t_osn)