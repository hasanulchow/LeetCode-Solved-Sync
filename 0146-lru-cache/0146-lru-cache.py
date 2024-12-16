from collections import OrderedDict

class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with a fixed capacity.
        Uses an OrderedDict to maintain the order of insertion
        and enable efficient LRU operations.
        """
        self.data: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if it exists in the cache.
        If the key is found, it is moved to the end to indicate
        it was recently used.
        Returns -1 if the key does not exist.
        """
        if key not in self.data:
            return -1
        # Move the key to the end (most recently used).
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key. If the key already exists,
        update its value and mark it as recently used by moving it to the end.
        If the cache exceeds its capacity, remove the least recently used item.
        """
        if key in self.data:
            # If the key exists, move it to the end.
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            # Remove the least recently used item (first item).
            self.data.popitem(last=False)

# Usage example:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
