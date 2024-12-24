class RandomizedCollection:

    def __init__(self):
        self.item_dict = dict() # needed for O(1) insert and remove (values are the keys of dict())
        self.item_list = list() # needed for O(1) random selection

    def insert(self, val: int) -> bool:
        if val in self.item_dict: # O(1) if value present in dict (cant have 0 occurances)
            self.item_dict[val].add(len(self.item_list)) # O(1) store new list index of value
            self.item_list.append(val) # O(1) add value to list
            return False
        else:
            self.item_dict[val] = {len(self.item_list)} # O(1) k-v pair where v is set of indexes
            self.item_list.append(val) # O(1) add value to list
            return True

    def remove(self, val: int) -> bool:
        if val in self.item_dict:
            swap_val = self.item_list[-1] # O(1) take last val in list
            ind = self.item_dict[val].pop() # O(1) delete and assign an index from set of indexes
            self.item_list[ind] = swap_val # O(1) put swap_val in place of val
            self.item_list.pop() # O(1) remove last value from list
            self.item_dict[swap_val].add(ind) # O(1) add swap_val's new index to index set
            self.item_dict[swap_val].discard(len(self.item_list)) # O(1) remove index of poped val
            if len(self.item_dict[val]) == 0: # O(1) k-v pair has zero occurances
                del self.item_dict[val] # O(1) delete k-v pair
            return True
        else:
            return False

    def getRandom(self) -> int:
        item = random.choice(self.item_list) # O(1)
        return item
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()