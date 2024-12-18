class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Finds the k-th factor of a given number n.

        :param n: int - The number whose factors are to be considered.
        :param k: int - The k-th position of the factor to find.
        :return: int - The k-th factor if it exists, otherwise -1.
        """
        # Initialize a counter to track the number of factors found so far.
        count = 0

        # Iterate through all numbers from 1 to n (inclusive).
        for i in range(1, n + 1):
            # Check if the current number 'i' is a factor of 'n'.
            if n % i == 0:
                count += 1  # Increment the factor counter.

                # If the k-th factor is found, return it.
                if count == k:
                    return i

        # If less than k factors are found, return -1 as the k-th factor does not exist.
        return -1
