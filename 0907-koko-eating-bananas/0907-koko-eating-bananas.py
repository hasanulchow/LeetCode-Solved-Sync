from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Function to check if it's possible to eat all bananas at speed `k` within `h` hours
        def canEatAll(piles, k, h):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k  # This formula computes the number of hours to eat each pile
            return time <= h  # Return True if total time is within the allowed hours

        # Binary search to find the minimum possible eating speed
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canEatAll(piles, mid, h):
                high = mid  # Try a smaller speed if we can finish in time
            else:
                low = mid + 1  # Increase speed if we cannot finish in time
        return low  # The smallest possible speed that works

# Example usage
sol = Solution()
piles = [3, 6, 7, 11]
h = 8
print(sol.minEatingSpeed(piles, h))  # Expected output: 4
