class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        res = 0
        freq = {}
        n = len(nums)
        for i in range(n):
            for j in range(n):
                t = nums[i]&nums[j]
                if t not in freq:
                    freq[t] = 0
                freq[t] += 1
        
        for n in nums:
            for t in freq:
                if n&t == 0:
                    res += freq[t]
        return res

        