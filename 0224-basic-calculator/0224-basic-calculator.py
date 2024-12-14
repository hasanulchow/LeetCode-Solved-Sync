class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        number = 0  # To store the current number being formed
        sign_value = 1  # To track the current sign (+1 or -1)
        result = 0  # To accumulate the result of the expression
        operations_stack = []  # Stack to store intermediate results and signs for '('

        # Iterate through each character in the string
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                number = number * 10 + int(c)  # Handles multi-digit numbers

            # If the character is '+' or '-', process the previous number
            elif c in "+-":
                result += number * sign_value  # Add the last number to the result
                sign_value = -1 if c == '-' else 1  # Update the sign for the next number
                number = 0  # Reset the current number for the next part of the expression

            # If the character is '(', push the current result and sign to the stack
            elif c == '(':
                operations_stack.append(result)  # Store current result
                operations_stack.append(sign_value)  # Store current sign
                result = 0  # Reset result for the sub-expression inside parentheses
                sign_value = 1  # Reset sign to default for the sub-expression

            # If the character is ')', compute the result for the parentheses
            elif c == ')':
                result += sign_value * number  # Add the last number before ')'
                number = 0  # Reset number after processing
                result *= operations_stack.pop()  # Multiply by the sign before '('
                result += operations_stack.pop()  # Add the result calculated before '('

        # After processing all characters, add the last number to the result
        return result + number * sign_value
