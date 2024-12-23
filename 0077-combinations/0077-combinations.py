class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Result list to store all combinations
        res = []
        # Temporary list to store the current combination
        comb = []

        # Backtracking function
        def backtrack(start):
            # If the combination has reached the required size, add it to the result
            if len(comb) == k:
                res.append(comb[:])  # Append a copy of the current combination
                return

            # Iterate over the numbers from 'start' to 'n'
            for num in range(start, n + 1):
                # Add the current number to the combination
                comb.append(num)
                # Recursively build the combination with the next number
                backtrack(num + 1)
                # Backtrack by removing the last added number
                comb.pop()

        # Start the backtracking process with the first number
        backtrack(1)
        return res
