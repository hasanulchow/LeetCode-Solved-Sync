class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Precompute lengths of strictly increasing subarrays from each index
        inc_len = [1] * n  # inc_len[i] will store the length of the longest strictly increasing subarray starting at index i
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_len[i] = inc_len[i + 1] + 1
        
        # Step 2: Find the maximum value of k
        max_k = 0
        
        for k in range(1, n // 2 + 1):  # Try all k from 1 to n//2
            for i in range(n - 2 * k + 1):  # The first subarray starts at index i, second subarray starts at index i + k
                if inc_len[i] >= k and inc_len[i + k] >= k:
                    max_k = k  # Update max_k if valid k is found
                    break  # No need to check further, as we found a valid k for this length
        
        return max_k