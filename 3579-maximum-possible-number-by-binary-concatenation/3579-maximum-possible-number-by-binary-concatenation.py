class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        def num_to_bin(num):
            s = ''
            while num:
                if num & 1:
                    s += '1'
                else:
                    s += '0'
                num = num >> 1
            return s[::-1]
            
        def bin_to_num(s):
            num = 0
            for idx, char in enumerate(s):
                num = num << 1
                num = num | int(char)
            return num

        nums = [num_to_bin(x) for x in nums]

        def dfs(s, picked=set()):
            if len(picked) == len(nums):
                possible.append(s)
                return

            for i in range(len(nums)):
                if i in picked:
                    continue
                picked.add(i)
                dfs(s + nums[i], picked)
                picked.remove(i)

        possible = []
        dfs('', set())

        numbers = [bin_to_num(x) for x in possible]
        
        return max(numbers)
        