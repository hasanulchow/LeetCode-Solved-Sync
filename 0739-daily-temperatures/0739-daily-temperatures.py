from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # The array to store the answer
        ans = [0] * len(temperatures)
        # Stack to store indices of the temperature array
        stack = []

        # Iterate through each temperature by its index
        for curr in range(len(temperatures)):
            # Check if the current temperature is higher than the temperature at the index stored in the stack
            while stack and temperatures[curr] > temperatures[stack[-1]]:
                # Pop the index from the stack and calculate the number of days to wait
                prev_index = stack.pop()
                ans[prev_index] = curr - prev_index  # The number of days between the current and the previous warmer day
            
            # Push the current index onto the stack
            stack.append(curr)

        return ans
