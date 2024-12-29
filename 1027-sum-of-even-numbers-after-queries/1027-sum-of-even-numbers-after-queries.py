class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for val in nums:
            if not val % 2:
                even_sum += val
        ans = []

        for query in queries:
            val, idx = query
            if (nums[idx] % 2):
                nums[idx] += val
                if (not nums[idx] % 2):
                    even_sum += nums[idx]
            else:
                temp = nums[idx]
                nums[idx] += val
                if (nums[idx] % 2):
                    even_sum -= temp
                else:
                    even_sum += nums[idx] - temp
            ans.append(even_sum)
        return ans