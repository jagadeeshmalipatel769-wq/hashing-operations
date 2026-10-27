class HashTable:
    def __init__(self, initial_size=4):
        self.table = [[] for _ in range(initial_size)]
        self.entry_count = 0
        self.load_factor_threshold = 0.7

    def _hash_function(self, key, size):
        return sum(ord(c) for c in key) % size

    def _rehash(self):
        new_size = len(self.table) * 2
        new_table = [[] for _ in range(new_size)]

        for bucket in self.table:
            for key, value in bucket:
                new_index = self._hash_function(key, new_size)
                new_table[new_index].append((key, value))

        self.table = new_table
        print(f"Rehashed! New table size: {new_size}")

    def insert(self, key, value):
        current_load_factor = (self.entry_count + 1) / len(self.table)
        if current_load_factor > self.load_factor_threshold:
            self._rehash()
        index = self._hash_function(key, len(self.table))
        self.table[index].append((key, value))
        self.entry_count += 1


ht = HashTable(4)

ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("cherry", 3)
ht.insert("date", 4)