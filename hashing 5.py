TABLE_SIZE = 1000
PRIME = 31


def polynomial_hash(key):
    hash_value = 0
    power = 1

    for c in key:
        hash_value = (hash_value + (ord(c) - ord('a') + 1) * power) % TABLE_SIZE
        power = (power * PRIME) % TABLE_SIZE

    return hash_value


def sum_hash(key):
    return sum(ord(c) for c in key) % TABLE_SIZE


print(f'"listen" sum hash: {sum_hash("listen")}, polynomial hash: {polynomial_hash("listen")}')
print(f'"silent" sum hash: {sum_hash("silent")}, polynomial hash: {polynomial_hash("silent")}')