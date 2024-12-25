class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the number of '1' bits in the binary representation of the given integer.

        Args:
        n (int): The input unsigned integer.

        Returns:
        int: The Hamming weight, i.e., the count of '1' bits in the binary representation of `n`.
        """
        # Convert the integer to its binary representation using bin() and count the '1's
        return bin(n).count("1")
