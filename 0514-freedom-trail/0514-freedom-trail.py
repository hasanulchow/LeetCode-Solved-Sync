class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R, K = len(ring), len(key)

        @functools.cache
        # r - current position of ring; k - index of key char
        def dp(r, k):
            # all characters in key have been spelled out
            if k == K: return 0

            char = key[k]

            # the current key character is on the ring's aligned position
            if ring[r] == char: return dp(r, k + 1) + 1

            # find steps needed to align ring to current key character by rotating clockwise
            pos_cw, cnt_cw = r, 0
            while ring[pos_cw] != char:
                pos_cw = pos_cw + 1 if pos_cw < R - 1 else 0
                cnt_cw += 1
            
            # find steps needed to align ring to current key character by rotating counter-clockwise
            pos_ccw, cnt_ccw = r, 0
            while ring[pos_ccw] != char:
                pos_ccw = pos_ccw - 1 if pos_ccw > 0 else R - 1
                cnt_ccw += 1
            
            return min(dp(pos_cw, k + 1) + cnt_cw + 1, dp(pos_ccw, k + 1) + cnt_ccw + 1)

        # r == 0 corresponds to 12:00 as per problem specification
        return dp(0, 0)