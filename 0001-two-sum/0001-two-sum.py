class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the value and index of each number
        numMap = {}
        n = len(nums)  # Get the length of the nums list

        # Iterate over the nums list
        for i in range(n):
            # Calculate the complement that, when added to nums[i], equals the target
            complement = target - nums[i]
            
            # Check if the complement exists in the dictionary
            if complement in numMap:
                # If found, return the indices of the complement and the current number
                return [numMap[complement], i]
            
            # Store the current number with its index in the dictionary
            numMap[nums[i]] = i

        # Return an empty list if no such pair exists
        return []
