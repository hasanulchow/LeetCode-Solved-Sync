class Solution:
    # DP Approach - Similar to 1143. Longest Common Subsequence
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # dp[i][j] means the length of repeated subarray of nums1[:i] and nums2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if both character is same
                if nums1[i - 1] == nums2[j - 1]:
                    # then we add 1 to the previous state, which is dp[i - 1][j - 1]
                    # in other word, we extend the repeated subarray by 1
                    # e.g. a = [1], b = [1], length of repeated array is 1
                    #      a = [1,2], b = [1,2], length of repeated array is the previous result + 1 = 2
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # record the max ans here
                    ans = max(ans, dp[i][j])
                # else:
                    # if you are looking for longest common sequence,
                    # then you put dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); here
                    # however, this problem is looking for subarray,
                    # since both character is not equal, which means we need to break it here
                    # hence, set dp[i][j] to 0
        return ans