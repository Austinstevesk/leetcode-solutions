max_hash_table_size = 4096

data_list = [None] * max_hash_table_size


def get_index(data_list, string):
    result = 0
    
    for char in string:
        result += ord(char)
    idx = result % len(data_list)
    return idx

def get_valid_index(data_list, key):
    idx = get_index(data_list, key)
    
    while True:
        kv = data_list[idx]
        
        if kv is None:
            return idx
        k, v = kv
        if key == k:
            return idx
        idx += 1
        
        if idx == len(data_list) - 1:
            idx = 0

class BasicHashTable:
    def __init__(self, max_size = max_hash_table_size) -> None:
        self.data_list = [None] * max_size
    
    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
    
    
    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)
    
    def get_all(self):
        return [kv for kv in self.data_list if kv is not None]

hash_table = BasicHashTable(1024)
hash_table.insert("Aust", "43625267255")
hash_table.insert("James", "5678972")
hash_table.insert("silent", "42567334")
hash_table.insert("listen", "142367334")

print(hash_table.find("Aust"))
hash_table.update("Aust", "563673323")
print(hash_table.find("Aust"))

print(hash_table.get_all())

print(get_valid_index(hash_table.data_list, key="listen"))
print(get_valid_index(hash_table.data_list, key="silent"))

print(hash_table.find("silent") == "42567334")
print(hash_table.find("listen") == "142367334")

# python friendly interface
class HashTable:
    def __init__(self, max_size=1) -> None:
        self.data_list = [None] * max_size
    
    def __get_valid_index__(self, key):
        idx = hash(key) % len(self.data_list)
        while True:
            k = self.data_list[idx]
            if k is None:
                return idx
            if k == key:
                return idx
            idx += 1
            if idx == len(self.data_list) - 1:
                idx = 0