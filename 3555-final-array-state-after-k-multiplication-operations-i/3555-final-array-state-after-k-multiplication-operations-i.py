class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Iterate k times, as the operation of multiplying the smallest element 
        # by the multiplier is to be performed k times.
        for _ in range(k):
            # Find the index of the smallest element in the nums array.
            x = nums.index(min(nums))  # `min(nums)` finds the smallest value, and `.index()` gets its index.
            
            # Multiply the smallest element by the multiplier and update the list.
            nums[x] *= multiplier  # Update the element at index x.
        
        # Return the modified nums list after k iterations.
        return nums
