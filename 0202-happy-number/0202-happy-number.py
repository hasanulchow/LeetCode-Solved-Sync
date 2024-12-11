class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to keep track of numbers we've already visited to avoid infinite loops
        visit = set()

        # Helper function to calculate the next number in the sequence
        def get_next_number(n):
            output = 0  # Initialize the sum of squares
            while n:  # Loop until n becomes 0
                digit = n % 10  # Get the last digit
                output += digit ** 2  # Add the square of the digit to the output
                n = n // 10  # Remove the last digit
            return output

        # Main loop to check if the number is happy
        while n not in visit:
            visit.add(n)  # Add the current number to the visited set

            n = get_next_number(n)  # Calculate the next number in the sequence

            if n == 1:  # If the number becomes 1, it is a happy number
                return True

        # If the loop ends, it means the sequence has entered a cycle (not a happy number)
        return False
