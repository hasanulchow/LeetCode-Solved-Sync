class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        m = defaultdict(int)
        for e in arr:
            m[e] += 1
        n = len(arr)
        mod = 10**9 + 7
        ans = 0
        for i in range(n):
            m[arr[i]] -= 1
            for j in range(i+1, n):
                m[arr[j]] -= 1
                left = target - arr[i] - arr[j]
                if m[left] > 0:
                    ans += m[left]; ans %= mod
            for j in range(i+1, n):
                m[arr[j]] += 1
        return ans