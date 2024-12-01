from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def df(start, path, currSum):
            # Base case: If we have k numbers in path and the sum is exactly n
            if len(path) == k and currSum == n:
                res.append(path)
                return
            # If we have k numbers but the sum is not equal to n, stop the search
            elif len(path) == k:
                return

            # Try to add each number from 'start' to 9
            for i in range(start, 10):
                # Recurse with the next number, path updated, and sum updated
                df(i + 1, path + [i], currSum + i)

        # Start the recursion with 1 as the first number, an empty path, and 0 sum
        df(1, [], 0)
        return res
