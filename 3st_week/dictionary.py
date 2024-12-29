class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        print(hash(key))
        print(idx)
        self.items[idx] = value

    def get(self, key):
        return self.items[hash(key) % len(self.items)]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))


class Dict2:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):



