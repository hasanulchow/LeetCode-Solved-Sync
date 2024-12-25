class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize a dictionary to store the frequency of cumulative sums, with 0 as the initial sum.
        sub_num = {0: 1}
        
        # Initialize total (cumulative sum) and count (number of subarrays that sum to k).
        total = count = 0

        # Iterate through the numbers in the input list 'nums'.
        for n in nums:
            # Update the cumulative sum with the current number 'n'.
            total += n
            
            # Check if there exists a subarray that sums to 'k'.
            # If 'total - k' is found in 'sub_num', it means there is a subarray whose sum is 'k'.
            if total - k in sub_num:
                # Add the number of times 'total - k' has appeared in 'sub_num' to the count.
                count += sub_num[total - k]
            
            # Update the frequency of the current cumulative sum 'total'.
            sub_num[total] = 1 + sub_num.get(total, 0)
        
        # Return the total count of subarrays whose sum equals 'k'.
        return count
