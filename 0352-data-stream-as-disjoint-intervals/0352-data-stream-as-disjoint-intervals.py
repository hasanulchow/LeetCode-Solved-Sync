from collections import deque

class SummaryRanges:
    def __init__(self):
        self.stack = deque()
        
    def dfs(self, nums):
        # Compute the intervals based on sorted and unique starts and ends
        return list(zip(sorted(set([n for n in nums if n-1 not in nums])),
                        sorted(set([n for n in nums if n+1 not in nums]))))

    def addNum(self, val):
        self.stack.append(val)  # Add the number to the stack

    def getIntervals(self):
        return self.dfs(self.stack)  # Return the computed intervals

# Example Usage:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
obj.addNum(7)
obj.addNum(2)
obj.addNum(6)
print(obj.getIntervals())  # Output: [(1, 2), (3, 3), (6, 7)]
