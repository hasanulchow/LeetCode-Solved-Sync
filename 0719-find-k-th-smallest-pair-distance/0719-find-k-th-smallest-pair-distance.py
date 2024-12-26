class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def findcnt(nums, dis, n, k):
            cnt = 0
            for i in range(n):
                s = i
                e = n - 1
                while s <= e:
                    m = s + (e - s) // 2
                    if (nums[m] - nums[i]) <= dis:
                        s = m + 1
                    else:
                        e = m - 1
                cnt += (e - i)
                if cnt >= k:
                    return cnt
            return cnt
        
        s = 0
        e = nums[n - 1] - nums[0]
        while s <= e:
            m = s + (e - s) // 2
            cnt = findcnt(nums, m, n, k)
            if cnt < k:
                s = m + 1
            else:
                e = m - 1
        return s