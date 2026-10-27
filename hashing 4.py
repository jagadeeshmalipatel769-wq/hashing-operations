TABLE_SIZE = 7


def hash_function(key):
    return sum(ord(c) for c in key) % TABLE_SIZE


class HashMap:
    def __init__(self):
        self.table = [[] for _ in range(TABLE_SIZE)]

    def put(self, key, value):
        index = hash_function(key)
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = hash_function(key)
        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value
        return None


class HashSet:
    def __init__(self):
        self.map = HashMap()

    def add(self, key):
        self.map.put(key, "present")

    def contains(self, key):
        return self.map.get(key) is not None


phone_book = HashMap()
phone_book.put("Ravi", "555-1234")
print("Ravi's number:", phone_book.get("Ravi"))

visited_cities = HashSet()
visited_cities.add("Mumbai")

print("Visited Mumbai?", "yes" if visited_cities.contains("Mumbai") else "no")
print("Visited Delhi?", "yes" if visited_cities.contains("Delhi") else "no")
