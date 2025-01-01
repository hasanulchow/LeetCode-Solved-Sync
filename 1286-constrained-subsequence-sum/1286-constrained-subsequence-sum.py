class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        SUM, IND = 0, 1

        if all(num < 0 for num in nums):
            return max(nums)

        heap = [(0, math.inf)]
        maxSum = -math.inf
        for i, num in enumerate(nums):
            while i - heap[0][IND] > k:
                heappop(heap)
                
            summ = -heap[0][SUM] + num
            maxSum = max(maxSum, summ)
            heappush(heap, (-summ, i))
        
        return maxSum