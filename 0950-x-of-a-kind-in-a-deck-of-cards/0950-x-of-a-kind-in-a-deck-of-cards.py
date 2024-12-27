# Dev: Chumicat
# Date: 2019/12/1
# Submission: https://leetcode.com/submissions/detail/282916566/
# (Time, Space) Complexity : O(n), O(n)

from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Rule:
        #   We just need to check if nums count are interprime
        #   If they have same prime factor, X must exist
        # Strategy:
        #   1. Get all count of each number
        #   2. Use gcd to check
        #   3. Return result
        
        # 1. Get all count of each number
        #    I take value from set arbitrarily rather than pop
        #    So that I didn't need to dealing one value case
        cnt_set = set(Counter(deck).values())
        gcd_val = next(iter(cnt_set))
        
        # 2, 3. Use gcd to check, return result
        for cnt in cnt_set:
            gcd_val = gcd(gcd_val, cnt)
            if gcd_val == 1: return False
        return True