from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        is_flipped = 0
        flip_positions = deque()
        
        for i in range(n):
            if flip_positions and flip_positions[0] == i:
                flip_positions.popleft()
                is_flipped ^= 1
            
            if nums[i] == is_flipped:
                if i + k > n:
                    return -1
                flip_positions.append(i + k)
                is_flipped ^= 1
                flips += 1
        
        return flips