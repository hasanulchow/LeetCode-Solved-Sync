class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ret = 1
        cur_max = max_ = nums[0]
        for i, n in enumerate(nums):
            if n < cur_max:
                cur_max = max_
                ret = i + 1
            if n > max_:
                max_ = n
        return ret