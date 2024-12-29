class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k,v in self.items:
            if k == key:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        print(hash(key))
        print(idx)
        self.items[idx] = value

    def get(self, key):
        return self.items[hash(key) % len(self.items)]


linked_tuple = LinkedTuple()
linked_tuple.add("333", 7)
linked_tuple.add("77", 6)

print(linked_tuple.get("333"))
print(linked_tuple.get("77"))
