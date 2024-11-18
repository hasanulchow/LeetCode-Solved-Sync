from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n, code = len(code), list(accumulate(code+code))
        if k < 0:
            return [code[i] - code[i+k] for i in range(n-1, 2*n-1)]
        if k > 0:
            return [code[i+k] - code[i] for i in range(n)]
        return [0] * n
