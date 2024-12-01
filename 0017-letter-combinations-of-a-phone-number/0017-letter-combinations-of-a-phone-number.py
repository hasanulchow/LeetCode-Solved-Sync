from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the digits string is empty, no combinations can be formed
        if not digits:
            return []
        
        # Mapping from digits to corresponding letters on a phone keypad
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # List to store the result
        self.ans = []

        # Backtracking helper function
        def backtrack(idx, current_combination):
            # Base case: If the current combination has reached the length of digits, add it to the result
            if idx == len(digits):
                self.ans.append(current_combination)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[idx]
            possible_letters = digit_to_char[current_digit]
            
            # Iterate over each letter corresponding to the current digit and recurse
            for letter in possible_letters:
                # Add the current letter to the combination and move to the next digit
                backtrack(idx + 1, current_combination + letter)
        
        # Start backtracking from the first digit with an empty string as the current combination
        backtrack(0, "")
        
        return self.ans
