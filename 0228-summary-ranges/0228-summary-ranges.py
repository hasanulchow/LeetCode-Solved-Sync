class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # If the input list is empty, return it directly as there are no ranges to summarize.
        if not nums:
            return nums
        
        # Initialize the start and end of the current range.
        start = nums[0]
        end = nums[0]
        res = []  # List to store the summarized ranges.
        
        # Iterate through the list, starting from the second element.
        for i in range(1, len(nums)):
            print(i)  # Debugging line, can be removed after testing.
            
            # Check if the current number is not consecutive with the previous number.
            if nums[i] != nums[i - 1] + 1:
                # Add the current range to the result list.
                if start == end:  # If the range consists of a single number.
                    res.append(f'{start}')
                else:  # If the range has multiple numbers.
                    res.append(f'{start}->{end}')
                
                # Reset the start and end to the current number for a new range.
                start = nums[i]
                end = nums[i]
            else:
                # Extend the current range by updating the end.
                end = nums[i]
        
        # Add the final range to the result list after the loop ends.
        if start != end and f'{start}->{end}' not in res:
            res.append(f'{start}->{end}')
        elif f'{end}' not in res:
            res.append(f'{start}')
        
        return res
