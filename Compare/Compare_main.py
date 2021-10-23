from POST.GET import SendGet
from cache.imbacash import imbacash
from Compare.Compare_class import Compare
import json

a=SendGet()
data=a.full_info(71031) # получение json по API

main_dict = imbacash() # получение плана после кэширования

a =Compare()
a.compare_dicts(data, main_dict) # сравнение плана и полученных результатов

