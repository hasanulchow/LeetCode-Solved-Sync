class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = deque(sorted(queries))
        available = []
        working = []
        for i in range(len(nums)):
            while q and q[0][0] <= i:
                heappush(available, -q.popleft()[1])
            while working and working[0] < i:
                heappop(working)
            while nums[i] > len(working):
                if available and -available[0] >= i:
                    heappush(working, -heappop(available))
                else:
                    return -1
        return len(available)