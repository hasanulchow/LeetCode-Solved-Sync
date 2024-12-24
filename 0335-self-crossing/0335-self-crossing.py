class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        N = len(x)
        for i in range(3, N):
            # Check the first condition: The current step crosses a previous one
            if i >= 3 and x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True

            # Check the second condition: A step creates a loop by matching with a previous one
            if i >= 4 and x[i - 1] == x[i - 3] and x[i - 2] <= x[i] + x[i - 4]:
                return True

            # Check the third condition: The path crosses itself in a more complex pattern
            if i >= 5 and x[i - 2] >= x[i - 4] and x[i - 3] - x[i - 5] <= x[i - 1] <= x[i - 3] and x[i] >= x[i - 2] - x[i - 4]:
                return True
        
        return False
