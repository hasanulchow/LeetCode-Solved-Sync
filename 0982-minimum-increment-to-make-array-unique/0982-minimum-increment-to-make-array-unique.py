class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_n = min(nums)
        cnt = [0] * (max(nums)-min_n+len(nums))
        for n in nums:
            cnt[n-min_n] += 1
        step, total = 0, 0
        for c in cnt:
            step += c
            if step > 0:
                step -= 1
            total += step
        return total