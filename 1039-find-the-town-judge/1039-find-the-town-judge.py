class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        countTrust = [0] * (n + 1)

        for judge in trust:
            countTrust[judge[0]] -= 1
            countTrust[judge[1]] += 1

        for i in range(1, n + 1):
            if countTrust[i] == n - 1:
                return i

        return -1