class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a given 32-bit unsigned integer.

        Args:
        n (int): The input 32-bit unsigned integer.

        Returns:
        int: The unsigned integer formed by reversing the bits of `n`.
        """
        result = 0  # Initialize the result to store the reversed bits
        
        # Loop 32 times, as the input is a 32-bit unsigned integer
        for _ in range(32):
            bit = n & 1  # Extract the least significant bit of `n`
            result = (result << 1) | bit  # Shift `result` left and append the bit
            n >>= 1  # Right-shift `n` to process the next bit
            
        return result  # Return the reversed bits as an integer
