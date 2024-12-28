class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        cnt = [0 for _ in range(n + 1)]
        s = k = 0
        for i in range(n):
            while s + cnt[i] < nums[i]:
                k += 1
                if k - 1 >= len(queries): return False
                l, r = queries[k - 1]
                if r < i: continue
                cnt[max(l, i)] += 1
                cnt[r + 1] -= 1
            s += cnt[i]
        return k <= len(queries)