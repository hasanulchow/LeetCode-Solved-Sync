class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix = 0  # This will hold the parity of the prefix sum (0 for even, 1 for odd)
        count_even = 1  # Initial prefix sum (0) is even
        count_odd = 0
        result = 0
        
        for num in arr:
            # Only the parity matters, so add num % 2
            prefix = (prefix + (num & 1)) & 1  # Use bitwise & for efficiency
            
            if prefix == 1:
                result = (result + count_even) % MOD
                count_odd += 1
            else:
                result = (result + count_odd) % MOD
                count_even += 1
        
        return result
        