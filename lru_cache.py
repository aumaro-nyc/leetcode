class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val

    def put(self, key: int, value: int) -> None:
        if self.current_size < self.capacity:
            self.cache[key] = value
            self.current_size += 1
        elif key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            del self.cache[list(self.cache)[0]]
            self.cache[key] = value
