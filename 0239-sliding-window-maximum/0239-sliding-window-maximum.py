from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  # Result list to store the maximums of each sliding window
        q = deque()  # Deque to maintain the elements in the sliding window, ensuring the largest element is at the front

        # Iterate through the list of numbers
        for idx, num in enumerate(nums):
            # Pop elements from the deque while the current element is larger than the last element in the deque
            # This ensures that the largest element is always at the front of the deque
            while q and q[-1] < num:
                q.pop()
            
            # Add the current number to the deque
            q.append(num)

            # If the index is greater than or equal to `k` and the element at the front of the deque is
            # the element that is leaving the sliding window, remove it from the deque
            if idx >= k and nums[idx - k] == q[0]:
                q.popleft()
            
            # Once the sliding window has reached size `k`, append the maximum element (front of deque) to the result list
            if idx >= k - 1:
                res.append(q[0])

        return res  # Return the list of maximums for each sliding window
