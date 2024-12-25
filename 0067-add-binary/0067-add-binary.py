class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns the result as a binary string.

        Args:
        a (str): First binary string.
        b (str): Second binary string.

        Returns:
        str: The resulting binary string after addition.
        """
        carry = 0  # Initialize the carry for addition
        res = []   # List to store the result in reverse order
        
        # Start from the least significant digit (rightmost) of both strings
        idxA, idxB = len(a) - 1, len(b) - 1
        
        # Continue processing while there are digits left in `a` or `b` or there is a carry
        while idxA >= 0 or idxB >= 0 or carry == 1:
            # Add the digit from `a` if within bounds
            if idxA >= 0:
                carry += int(a[idxA])  # Convert character to integer and add to carry
                idxA -= 1             # Move to the next digit on the left
            
            # Add the digit from `b` if within bounds
            if idxB >= 0:
                carry += int(b[idxB])  # Convert character to integer and add to carry
                idxB -= 1             # Move to the next digit on the left

            # Append the current bit (carry % 2) to the result
            res.append(str(carry % 2))
            
            # Update the carry (carry // 2)
            carry = carry // 2
            
        # Join the result list in reverse order to form the final binary string
        return "".join(res[::-1])
