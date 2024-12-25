class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Computes the bitwise AND of all numbers in the range [left, right].
        
        Args:
        left (int): The starting number of the range.
        right (int): The ending number of the range.
        
        Returns:
        int: The result of the bitwise AND operation over all numbers in the range.
        """
        cnt = 0  # Counter to track the number of right shifts performed
        
        # Reduce the range by right-shifting both `left` and `right`
        # until they become equal. This eliminates differing bits.
        while left != right:
            left >>= 1  # Right shift `left` by 1 bit
            right >>= 1  # Right shift `right` by 1 bit
            cnt += 1  # Increment the shift counter
        
        # Shift the result back to the left by the same number of shifts
        # to account for the removed lower bits.
        return left << cnt
