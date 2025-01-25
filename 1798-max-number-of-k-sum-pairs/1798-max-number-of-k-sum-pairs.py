class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = 1

        """
        n^2 is 1,000,000,000 so no n^2

        brute force would take too long
        
        this is a variant of two sum.
        if we store the two sum, we know what indices we can immediately remove
        """
        h = defaultdict(list)
        for ni, n in enumerate(nums):
            h[n].append(ni)

        
        if len(h) == 1:  # edge case: all same number, like k=10, [5,5,5,5.........5,5]
            if list(h.keys())[0] == k / 2:
                return len(nums) // 2
            return 0

        used = set()  # no need to actually remove elements which would mess up all the indices in h
        ops = 0
        i = 0
        while nums and i < len(nums):
            if i in used:
                i += 1
                continue

            target = k - nums[i]
            if h.get(target) != []:
                for ind_i, ind in enumerate(h[target]):
                    if ind > i and ind not in used:
                        ops += 1
                        used.add(i)
                        used.add(ind)
                        break
            
            i += 1
        
        return ops