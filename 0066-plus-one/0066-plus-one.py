class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the list from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            
            # If the current digit is 9, set it to 0 and continue
            # This handles the carry to the next digit
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digit is not 9, increment it by 1
                digits[i] = digits[i] + 1
                return digits  # Return the updated list immediately, no further carry needed
        
        # If all digits were 9 (e.g., [9, 9, 9]), we need an additional digit for the carry
        # Prepend 1 to the list (e.g., [1, 0, 0, 0])
        return [1] + digits
