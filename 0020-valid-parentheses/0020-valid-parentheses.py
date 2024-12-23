class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        # Iterate through each character in the string
        for char in s:
            # If the character is one of the opening brackets, push it onto the stack
            if char in mapping.values():
                stack.append(char)
            # If the character is one of the closing brackets, check the stack
            elif char in mapping.keys():
                # If the stack is empty or the last opening bracket doesn't match the current closing bracket, return False
                if not stack or mapping[char] != stack.pop():
                    return False
        
        # If the stack is empty, all brackets matched correctly; otherwise, return False
        return not stack
