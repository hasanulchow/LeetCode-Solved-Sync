class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Initialize variables
        zero = 0
        one = 0
        totalzeroes = 0
        n = len(s)
        mn = float('inf')

        # Initialize an array to store the number of flips needed at each index
        res = [0] * n

        # Loop through the input string and count the total number of zeroes
        for i in s:
            if i == '0':
                totalzeroes += 1

        # Loop through the input string
        for i in range(n):
            # If the current character is '0', increment the zero count
            if s[i] == '0':
                zero += 1

            # Calculate the number of flips needed at this index
            res[i] = one + totalzeroes - zero

            # If the current character is '1', increment the one count
            if s[i] == '1':
                one += 1

            # Update the minimum number of flips needed if needed
            if mn > res[i]:
                mn = res[i]

        # Return the minimum number of flips needed
        return mn