from POST.GET import SendGet
from cache.imbacash import imbacash
from cache.LRUcache import LRUcache

a=SendGet()
data=a.full_info(71031)

#main_dict = imbacash()
#print(main_dict.get("num_tl"))

#a = Compare()
#a.compare_dicts(data, main_dict)

