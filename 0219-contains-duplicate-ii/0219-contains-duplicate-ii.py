class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each element
        seen = {}
        
        # Iterate through the list with index and value
        for i, val in enumerate(nums):
            # Check if the current value is already in the dictionary
            # and if the difference between the indices is less than or equal to k
            if val in seen and i - seen[val] <= k:
                return True  # Duplicate found within the allowed range
            
            # Update the dictionary with the current index of the value
            seen[val] = i

        # No duplicates found within the range
        return False
