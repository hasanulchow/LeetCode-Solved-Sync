class Solution:
    def judgeSquareSum(self, target: int) -> bool:
        if target <= 2:
            return True  # Early return for small values of target

        # Iterate from the square root of target down to 1
        for a in range(int(math.isqrt(target)), 0, -1):
            # Calculate the remaining value after subtracting the square of a
            remainder = target - a * a
            # Calculate the integer square root of the remainder
            b = int(math.isqrt(remainder))
            
            # Check if the square of b equals the remainder
            if b * b == remainder:
                return True  # If true, a^2 + b^2 = target, return true

        # If no pair (a, b) is found such that a^2 + b^2 = target, return false
        return False