from collections import OrderedDict
import requests
class LRUcache:

    def __init__ (self,capacity:int):
        self.size=capacity
        self.cache=OrderedDict()
      #  self.dict = dict
      #  self.file_output = file_output

    def get(self,key): # Получаем значение по ключу из кэша
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self,key,value): # Кладем данные в кэш
        if key not in self.cache:
            if len(self.cache)>=self.size:
                self.cache.popitem(last=False)

        else:
            self.cache.move_to_end(key)
        self.cache[key]=value
















