class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to keep track of previous strings and numbers
        curNum = 0  # Current number (multiplier for the string)
        curString = ''  # Current string being built

        for c in s:  # Iterate through each character in the string
            if c == '[':
                # Push the current string and the current number onto the stack
                stack.append(curString)
                stack.append(curNum)
                # Reset current string and number for the next substring
                curString = ''
                curNum = 0
            elif c == ']':
                # Pop the last number and string from the stack
                num = stack.pop()
                prevString = stack.pop()
                # Repeat the current string `num` times and append it to the previous string
                curString = prevString + num * curString
            elif c.isdigit():
                # Build the current number (for cases like "10[abc]")
                curNum = curNum * 10 + int(c)
            else:
                # Append the current character to the current string
                curString += c
        
        return curString
