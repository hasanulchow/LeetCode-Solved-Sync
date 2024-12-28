class Solution:
    def sumOfGoodSubsequences(self, nums):
        n, mod, count, total = len(nums), 10**9+7, defaultdict(int), defaultdict(int)

        for i in nums:
            count[i] += count[i-1] + count[i+1] + 1 
            total[i] += total[i-1] + total[i+1] + i*(count[i-1] + count[i+1] + 1)

        return sum(total.values())%mod 