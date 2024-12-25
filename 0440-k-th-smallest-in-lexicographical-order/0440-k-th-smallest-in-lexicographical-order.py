class Solution:
    def getReqNum(self, a, b, n):
        """
        Calculate the number of integers between `a` and `b` within the range [1, n].
        
        Args:
        a (int): The lower bound of the current range.
        b (int): The upper bound of the current range.
        n (int): The maximum number in the range [1, n].
        
        Returns:
        int: The count of integers in the current range.
        """
        gap = 0  # Initialize the count of numbers in the current range.
        while a <= n:
            # Add the number of integers in the current range, limited by n + 1.
            gap += min(n + 1, b) - a
            # Move to the next range by multiplying `a` and `b` by 10.
            a *= 10
            b *= 10
        return gap

    def findKthNumber(self, n: int, k: int) -> int:
        """
        Find the k-th smallest number in lexicographical order within the range [1, n].
        
        Args:
        n (int): The maximum number in the range [1, n].
        k (int): The target position (1-indexed) of the k-th smallest number.
        
        Returns:
        int: The k-th smallest number in lexicographical order.
        """
        num = 1  # Start with the first number in lexicographical order.
        i = 1    # Initialize the current position to 1.

        while i < k:
            # Calculate the number of integers between `num` and `num + 1` within the range.
            req = self.getReqNum(num, num + 1, n)
            
            if i + req <= k:
                # If the k-th number is not in the current range, move to the next sibling.
                i += req
                num += 1
            else:
                # If the k-th number is in the current subtree, move to the next level (child).
                i += 1
                num *= 10
        
        return num
