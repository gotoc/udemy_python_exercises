

class Memcache:
    def __init__(self):
        self.CACHE = {}

    def set(self, key, value):
        self.key = key
        self.value = value
        self.CACHE[key] = value
        return key, value

    def get(self, key):
        self.key = key
        return self.CACHE[key]

    def delete(self, key):
        self.key = key
        del self.CACHE[key]

    def flush(self):
        self.CACHE.clear()

def test_memcache():
    m = Memcache()
    print("set a: " + str(m.set('a', '1')))
    print("set b: " + str(m.set('b','2')))
    print(m.CACHE)
    print(m.get('b'))
    m.delete('b')
    m.flush()
    print("Cache After Flush: " + str(m.CACHE))

test_memcache()