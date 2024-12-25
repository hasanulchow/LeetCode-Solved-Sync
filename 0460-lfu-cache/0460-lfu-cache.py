from collections import deque, defaultdict

class Node:
    def __init__(self, key, value):
        """
        Node to store key-value pair along with its frequency.
        """
        self.key = key
        self.value = value
        self.freq = 1  # Initial frequency of access is 1

class LFUCache:

    def __init__(self, capacity: int):
        """
        Initializes the LFU Cache.
        Args:
        capacity (int): Maximum capacity of the cache.
        """
        self.capacity = capacity  # Cache capacity
        self.minFreq = 0  # Track the minimum frequency in the cache
        self.keyToNode = dict()  # Maps keys to their corresponding Node
        self.freqToList = defaultdict(deque)  # Maps frequency to deque of keys
        self.freqToKey = defaultdict(set)  # Maps frequency to a set of keys

    def get(self, key: int) -> int:
        """
        Retrieves the value for a given key if it exists, and updates its frequency.
        Args:
        key (int): The key to retrieve the value for.
        
        Returns:
        int: The value corresponding to the key, or -1 if the key does not exist.
        """
        if key not in self.keyToNode:
            return -1  # Key not found in cache
        
        # Retrieve the node and update its frequency
        node = self.keyToNode[key]
        self.touch(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair in the cache.
        If the cache is at capacity, it evicts the least frequently used item.
        Args:
        key (int): The key to insert or update.
        value (int): The value to associate with the key.
        """
        if self.capacity == 0:
            return  # Do nothing if the cache capacity is 0
        
        if key in self.keyToNode:
            # Update value if the key already exists
            node = self.keyToNode[key]
            node.value = value
            self.touch(node)
            return
        
        if len(self.keyToNode) == self.capacity:
            # Evict the least frequently used key
            keyToEvict = self.freqToList[self.minFreq].pop()
            self.freqToKey[self.minFreq].remove(keyToEvict)
            del self.keyToNode[keyToEvict]
        
        # Add the new key-value pair to the cache
        self.minFreq = 1
        self.freqToList[1].appendleft(key)
        self.freqToKey[1].add(key)
        self.keyToNode[key] = Node(key, value)

    def touch(self, node):
        """
        Updates the frequency of a given node when it is accessed or updated.
        Args:
        node (Node): The node whose frequency needs to be updated.
        """
        prevFreq = node.freq
        newFreq = node.freq + 1
        
        # Remove the key from the previous frequency list
        self.freqToList[prevFreq].remove(node.key)
        self.freqToKey[prevFreq].remove(node.key)
        
        # If the frequency list is empty, clean it up and adjust minFreq if necessary
        if len(self.freqToList[prevFreq]) == 0:
            del self.freqToList[prevFreq]
            if prevFreq == self.minFreq:
                self.minFreq += 1
        
        # Add the key to the new frequency list
        if newFreq not in self.freqToList:
            self.freqToList[newFreq] = deque()
            self.freqToKey[newFreq] = set()
            
        self.freqToList[newFreq].appendleft(node.key)
        self.freqToKey[newFreq].add(node.key)
        node.freq = newFreq  # Update the node's frequency
