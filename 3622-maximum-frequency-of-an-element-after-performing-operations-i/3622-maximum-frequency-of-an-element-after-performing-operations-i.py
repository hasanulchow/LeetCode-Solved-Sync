class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        # Sort the array to use a sliding window approach
        nums.sort()
        n = len(nums)
        ans = 0
        left = 0
        right = 0
        
        # First pass: choose existing numbers as reference points
        from collections import Counter
        count = Counter(nums)  # Dictionary to store frequency of each element

        for mid in range(n):
            # Move the left pointer to maintain the range within `k`
            while nums[mid] - nums[left] > k:
                left += 1

            # Move the right pointer to include numbers within `k` range from `nums[mid]`
            while right < n - 1 and nums[right + 1] - nums[mid] <= k:
                right += 1

            # Calculate total elements in the current range
            total = right - left + 1
            # Update ans with the maximum frequency achievable with current reference
            ans = max(ans, min(total - count[nums[mid]], numOperations) + count[nums[mid]])

        # Second pass: choose a non-existent midpoint as reference
        left = 0
        for right in range(n):
            # Calculate midpoint between nums[left] and nums[right]
            mid = (nums[left] + nums[right]) // 2
            # Move left pointer to keep midpoint within `k` range of both ends
            while mid - nums[left] > k or nums[right] - mid > k:
                left += 1
                mid = (nums[left] + nums[right]) // 2
            
            # Update ans with maximum frequency achievable with non-existent midpoint
            ans = max(ans, min(right - left + 1, numOperations))
        
        return ans