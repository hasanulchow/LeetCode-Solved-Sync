class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(n,i) for i, n in enumerate(nums)]
        marked = set()
        heapify(heap)
        res=0
        while heap:
            n, i = heappop(heap)
            if i in marked:
                continue

            marked.add(i-1)
            marked.add(i+1)
            res+=n

        return res
        