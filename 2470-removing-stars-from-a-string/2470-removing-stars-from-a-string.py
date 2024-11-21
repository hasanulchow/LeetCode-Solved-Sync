class Solution:
    def removeStars(self, s: str) -> str:
        s = s[::-1]  # Step 1: Reverse the string
        stk = ""  # Step 2: Initialize an empty string (acts as a stack)
        count = 0  # Step 3: Initialize a counter for the stars

        for i in s:  # Step 4: Iterate through each character in the reversed string
            if i == "*":  # Step 5: If the character is a star ('*')
                count += 1  # Increment the star counter (indicating the number of removals needed)
            elif count > 0 and i != "*":  # Step 6: If we have stars to remove and the character is not a star
                count -= 1  # Decrease the counter, effectively "removing" the previous character
            else:  # Step 7: If there are no stars to remove, add the character to the result string (stack)
                stk += i

        stk = stk[::-1]  # Step 8: Reverse the string again to restore the original order
        return stk  # Step 9: Return the final result (string after removals)
