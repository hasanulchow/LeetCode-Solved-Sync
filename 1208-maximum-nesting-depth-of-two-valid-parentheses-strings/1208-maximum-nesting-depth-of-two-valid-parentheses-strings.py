class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # T: O(N log(N)), S: O(N)
        N = len(seq)
        def test(targetDepth, output):
            depth, s = [0, 0], 0
            maxDepth = 0
            for i, c in enumerate(seq):
                if c == '(':
                    if depth[0] == targetDepth: s = 1
                    depth[s] += 1
                    output[i] = s
                else:
                    depth[s] -= 1
                    output[i] = s
                    if depth[1] == 0: s = 0

                maxDepth = max(maxDepth, depth[0], depth[1])
            return maxDepth <= targetDepth

        l, r = 0, N // 2
        ans = []            
        while l <= r:
            m = l + (r - l) // 2

            candidate = [0] * N
            if test(m, candidate):
                ans = candidate
                r = m - 1
            else:
                l = m + 1
        
        return ans