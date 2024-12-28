class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        edge_case_set = set()
        for num in nums:
            edge_case_set.add(num)
        if edge_case_set == {0}:
            return 0
        n, q = len(nums), len(queries)
        k = 0
        queries_change = [0]*n # Question gives 0 <= l <= r < n #Now only useful for unvisited nums
        n_start = 0
        change = 0
        for i in range(n):
            change += queries_change[i]
            nums[i] -= change
            while nums[i] > 0:
                if k == q:
                    return -1 # No more queries
                else:
                    l,r,val = queries[k][0], queries[k][1], queries[k][2]
                    k += 1
                    if r < i: # query redundant as only affects already visited (<= 0) numbers
                        continue
                    elif l > i: # query will only affect future numbers
                        queries_change[l] += val
                        if r < n-1:
                            queries_change[r+1] -= val
                    else: #query will add to change, to also adjust the negation of this change for future numbers in queries_change
                        nums[i] -= val
                        change += val
                        if r < n-1:
                            queries_change[r+1] -= val
        return k