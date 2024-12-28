class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:

        n, d, mn = len(nums), defaultdict(list), inf

        for i, num in enumerate(nums): d[num].append(i)

        for arr in d.values():
            arr.append(arr[0] + n)
            mx = max([j-i for i, j in pairwise(arr)])
            mn = min(mx, mn)

        return mn//2