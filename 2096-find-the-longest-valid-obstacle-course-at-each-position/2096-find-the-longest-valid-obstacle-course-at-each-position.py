class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack = [] # initialize an empty stack
        ans = []   # initialize an empty list to store the result
        
        for o in obstacles: # loop through each obstacle in the input list
            if not stack or o >= stack[-1]: # if the stack is empty or the current obstacle is greater than or equal to the top of the stack
                stack.append(o) # append the current obstacle to the stack
                ans.append(len(stack)) # append the length of the stack to the result
            else: # if the current obstacle is less than the top of the stack
                left, right = 0, len(stack) - 1 # initialize two pointers for binary search
                while left <= right: # perform binary search to find the index where the current obstacle should be inserted into the stack
                    mid = left + (right - left) // 2
                    if stack[mid] <= o:
                        left = mid + 1
                    else:
                        right = mid - 1
                stack[left] = o # replace the value at the found index with the current obstacle
                ans.append(left + 1) # append the found index + 1 to the result
        
        return ans # return the result