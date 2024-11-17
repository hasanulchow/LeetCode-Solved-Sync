class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Compute the prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Step 2: Use a deque to find the shortest subarray
        dq = deque()  # stores indices of the prefix array
        min_len = float('inf')  # Initialize to infinity
        
        for i in range(n + 1):
            # Step 3: Check for all previous indices in the deque that could form a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())  # Update the result with the shortest subarray length
            
            # Step 4: Maintain the deque (we need to keep it in increasing order of prefix sums)
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            # Step 5: Add the current index to the deque
            dq.append(i)
        
        # Step 6: Return the result
        return min_len if min_len != float('inf') else -1