import random

class RandomizedSet:
    """
    A data structure that supports insertion, deletion, and random retrieval of elements.
    The operations must be performed in average O(1) time complexity.
    """

    def __init__(self):
        """
        Initializes an empty RandomizedSet.
        - `values` will store the elements in the set.
        - `value_to_index` maps each element to its index in `values` for quick access during removal.
        """
        self.values = []  # List to store elements
        self.value_to_index = {}  # Dictionary to map element to its index in `values`
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value into the set if it doesn't already exist.
        Returns `True` if the element is successfully inserted, `False` if the element already exists.
        This operation is O(1) on average.
        """
        if val not in self.value_to_index:
            self.values.append(val)  # Append the new value at the end of the list
            self.value_to_index[val] = len(self.values) - 1  # Store the index of the value in the dictionary
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set if it exists.
        Returns `True` if the element is successfully removed, `False` if the element doesn't exist.
        This operation is O(1) on average.
        """
        if val in self.value_to_index:
            # Get the index of the value to remove
            index = self.value_to_index[val]
            # Move the last element to the position of the element to remove
            last_value = self.values[-1]
            self.values[index] = last_value
            self.value_to_index[last_value] = index  # Update the index of the last value

            # Remove the last element
            self.values.pop()
            del self.value_to_index[val]  # Remove the entry for the value from the dictionary
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Returns a random element from the set. The time complexity is O(1).
        This is done by using random.choice() on the `values` list.
        """
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
