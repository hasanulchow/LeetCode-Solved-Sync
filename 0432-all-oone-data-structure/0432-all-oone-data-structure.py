class AllOne:

    def __init__(self):
        # Initialize the data structures:
        # `self.d`: dictionary to store the count of each key.
        # `self.op`: tracks the last operation (1 for getMaxKey, 2 for getMinKey).
        # `self.res`: stores the result of the last operation to optimize repeated queries.
        self.d = {}  # Dictionary to store key counts
        self.op = 0  # Previous operation (0 for none, 1 for getMaxKey, 2 for getMinKey)
        self.res = ""  # Previous operation result (max or min key)

    def inc(self, key: str) -> None:
        """
        Increments the count of the given key. If the key does not exist, add it with count 1.
        Resets the operation type to 0 (since an operation has been performed).
        """
        self.op = 0  # Reset operation
        if key in self.d:
            self.d[key] += 1  # Increment the count if the key exists
        else:
            self.d[key] = 1  # Add key with count 1 if it does not exist
        return None

    def dec(self, key: str) -> None:
        """
        Decrements the count of the given key. If the count becomes 0, remove the key from the dictionary.
        Resets the operation type to 0 (since an operation has been performed).
        """
        self.op = 0  # Reset operation
        if self.d[key] > 1:
            self.d[key] -= 1  # Decrement the count if it's greater than 1
        else:
            del self.d[key]  # Remove the key if its count becomes 0
        return None

    def getMaxKey(self) -> str:
        """
        Returns the key with the maximum count.
        If the last operation was `getMaxKey`, return the cached result to avoid recalculating.
        """
        if self.op == 1:
            return self.res  # Return cached result if the last operation was `getMaxKey`
        self.op = 1  # Mark the current operation as `getMaxKey`
        
        if self.d:  # If the dictionary is not empty
            # Find the key with the maximum count
            a = list(self.d.values())[0]
            b = list(self.d.keys())[0]
            for key in self.d.keys():
                if self.d[key] > a:
                    a = self.d[key]
                    b = key
            self.res = b  # Cache the result
            return b
        self.res = ""  # Return empty string if the dictionary is empty
        return ""

    def getMinKey(self) -> str:
        """
        Returns the key with the minimum count.
        If the last operation was `getMinKey`, return the cached result to avoid recalculating.
        """
        if self.op == 2:
            return self.res  # Return cached result if the last operation was `getMinKey`
        self.op = 2  # Mark the current operation as `getMinKey`
        
        if self.d:  # If the dictionary is not empty
            # Find the key with the minimum count
            a = list(self.d.values())[0]
            b = list(self.d.keys())[0]
            for key in self.d.keys():
                if self.d[key] < a:
                    a = self.d[key]
                    b = key
            self.res = b  # Cache the result
            return b
        self.res = ""  # Return empty string if the dictionary is empty
        return ""

# Example usage:
obj = AllOne()

# Increment keys
obj.inc("key1")  # key1's count becomes 1
obj.inc("key2")  # key2's count becomes 1
obj.inc("key2")  # key2's count becomes 2

# Get the key with the maximum count
param_3 = obj.getMaxKey()  # Returns "key2" (max count)

# Get the key with the minimum count
param_4 = obj.getMinKey()  # Returns "key1" (min count)

# Decrement a key
obj.dec("key1")  # key1's count becomes 0 and is removed

# Get the updated maximum and minimum keys
param_5 = obj.getMaxKey()  # Returns "key2" (still the max key)
param_6 = obj.getMinKey()  # Returns "key2" (since key1 was removed)
