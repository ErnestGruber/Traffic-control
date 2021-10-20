import weakref
class SimpleCache:
    def __init__(self, cacheSize):
        self.cache = weakref.WeakValueDictionary()
        self.cache_LRU = []
        self.cacheSize = cacheSize

    def __getitem__(self, key):
        # no exception catching - let calling code handle them if any
        value = self.cache[key]
        return self.touchCache(key, value)

    def __setitem__(self, key, value):
        self.touchCache(key, value)

    def touchCache(self, key, value):
        self.cache[key] = value
        if value in self.cache_LRU:
            self.cache_LRU.remove(value)
        self.cache_LRU = self.cache_LRU[-(self.cacheSize-1):] + [ value ]
        return value