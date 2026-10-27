TABLE_SIZE = 10


def hash_function(key):
    total = sum(ord(c) for c in key)
    return total % TABLE_SIZE


keys = ["apple", "banana", "cherry"]

for key in keys:
    index = hash_function(key)
    print(f'"{key}" hashes to index: {index}')