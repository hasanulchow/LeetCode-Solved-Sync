class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 'replace' will keep track of the index where the next unique element should be placed
        replace = 1
        
        # Start from the second element and iterate through the list
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i-1] != nums[i]:
                # Place the current unique element at the 'replace' index
                nums[replace] = nums[i]
                # Increment 'replace' to point to the next position
                replace += 1
        
        # Return the new length of the list with unique elements
        return replace

        