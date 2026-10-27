TABLE_SIZE = 5


def hash_function(key):
    return sum(ord(c) for c in key) % TABLE_SIZE


class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(TABLE_SIZE)]

    def insert(self, key, value):
        index = hash_function(key)
        self.table[index].append((key, value))

    def find(self, key):
        index = hash_function(key)
        for stored_key, stored_value in self.table[index]:
            if stored_key == key:
                return stored_value
        return None


ht = HashTable()

ht.insert("cat", 1)
ht.insert("act", 2)

result = ht.find("act")
print("Found 'act' with value:", result)