class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Get the length of the original list
        length = len(nums)
        
        # Initialize a counter for the number of removed elements
        removed = 0
        
        # Iterate through each element in the list
        for el in nums:
            # If an element occurs more than twice in the list
            if nums.count(el) > 2:
                # Keep removing the element until it occurs exactly twice
                while nums.count(el) != 2:
                    nums.remove(el)  # Remove the element from the list
                    removed += 1  # Increment the removed count
        
        # Return the new length of the list after removal of extra duplicates
        return length - removed
